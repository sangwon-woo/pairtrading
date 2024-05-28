import time
import json
import uuid
import hashlib
import jwt
import websockets
import pandas as pd
import requests as rq
import config.setting as st
from multiprocessing import Process
from urllib.parse import urlencode
import asyncio


class UpbitMachine:
    """
    업비트 거래소와의 거래를 위한 클래스
    BASE_API_URL은 API 호출을 위한 기본 URL
    """

    BASE_API_URL = 'https://api.upbit.com/v1'

    def __init__(self) -> None:
        self.ACCESS_KEY = st.UPBIT_ACCESS_KEY
        self.SECRET_KEY = st.UPBIT_SECRET_KEY
        self.DIR_DATABASE = st.DIR_UPBIT_DATABASE
        self.access_token = None
        self.refresh_token = None

class QuotationAPI(UpbitMachine):
    """
    업비트 API 중 Quotation과 관련된 API
    1. 시세 종목 조회
        - 마켓 코드 조회 : 업비트에서 거래 가능한 마켓 목록
    2. 시세 캔들 조회
        - 분 캔들 : 분 캔들 조회
        - 일 캔들 : 일 캔들 조회
        - 주 캔들 : 주 캔들 조회
        - 월 캔들 : 월 캔들 조회
    3. 시세 체결 조회
        - 최근 체결 내역 : 체결 내역 조회
    4. 시세 Ticker 조회
        - 현재가 정보 : 요청 당시 종목의 스냅샷 조회
    5. 시세 호가 정보 조회
        - 호가 정보 조회 : 요청 당시 종목의 호가 정보 조회(1호가부터 15호가까지)
    """

    def __init__(self) -> None:
        super().__init__()
        self.headers = {
            'Accept': 'application/json'
        }

    def get_market_code(self, is_details=False) -> pd.DataFrame:
        """
        업비트에서 거래 가능한 마켓 목록 조회

        Parameters
        ----------
        is_details : Bool
            유의종목 필드와 같은 상세 정보 노출 여부. 기본값은 False
        """
        df = pd.DataFrame()
        is_details = 'false' if is_details == False else 'true'
        url = self.BASE_API_URL + '/market/all?isDetails={}'.format(is_details)

        # try - except
        res = rq.get(url, headers=self.headers)

        return pd.DataFrame(res.json())

    def get_minute_candle(self, unit=1, market='KRW-BTC', to=None, count=1) -> pd.DataFrame:
        """
        특정 화폐의 분봉 조회
        ----------

        Parameters
        ----------
        unit : int
            분봉의 단위. 기본값은 1
            가능한 값 : 1, 3, 5, 10, 15, 30, 60, 240
        market : string
            마켓 코드. 기본값은 KRW-BTC
        to : string
            마지막 캔들 시각(exclusive). 기본값은 None 
            포맷 : yyyy-MM-dd HH:mm:ss
        count : int
            캔들 갯수. 기본값은 1. 최대 200개까지 요청 가능. 
        """
        df = pd.DataFrame()
        base_url = self.BASE_API_URL + '/candles/minutes/{}?'.format(unit)

        if to:
            print(f'{market} => {to}보다 이전 {unit}분봉 데이터 조회')
            to = to.replace(' ', '%20').replace(':', '%3A')
            query = 'market={}&to={}&count={}'.format(market, to, count)
        else:
            query = 'market={}&count={}'.format(market, count)

        url = base_url + query

        # try - except
        res = rq.get(url, headers=self.headers).json()
        time.sleep(0.12)
        
        return pd.DataFrame(res)

    def get_day_candle(self, market='KRW-BTC', to=None, count=1, converting_price_unit=None) -> pd.DataFrame:
        """
        특정 화폐의 일봉 조회

        Parameters
        ----------
        market : string
            마켓 코드. 기본값은 KRW-BTC
        to : string
            마지막 캔들 시각(exclusive). 기본값은 None
            포맷 : yyyy-MM-dd HH:mm:ss
        count : int
            캔들 갯수. 기본값은 1. 최대 200개까지 요청 가능. 
        converting_price_unit : string
            원화 마켓이 아닌 다른 마켓의 일봉 요청시 종가를 명시된 파라미터 값으로 환산. 기본값은 None.
            현재는 원화(KRW)로 변환하는 기능만 제공하며 추후 기능을 확장할 수 있음. 
        """
        df = pd.DataFrame()
        base_url = self.BASE_API_URL + '/candles/days?'

        if to:
            if converting_price_unit:
                print(
                    f'{market} => {to}보다 이전 일봉 데이터 및 {converting_price_unit}로 환산하여 조회')
                to = to.replace(' ', '%20').replace(':', '%3A')
                query = 'market={}&to={}&count={}&convertingPriceUnit={}'.format(
                    market, to, count, converting_price_unit)
            else:
                print(f'{market} => {to}보다 이전 일봉 데이터 조회')
                to = to.replace(' ', '%20').replace(':', '%3A')
                query = 'market={}&to={}&count={}'.format(market, to, count)
        else:
            if converting_price_unit:
                print(f'{market} => {converting_price_unit}로 환산하여 조회')
                query = 'market={}&count={}&convertingPriceUnit={}'.format(
                    market, count, converting_price_unit)
            else:
                query = 'market={}&count={}'.format(market, count)

        url = base_url + query

        # try - except
        res = rq.get(url, headers=self.headers).json()
        time.sleep(0.1)

        for i in range(len(res)):
            dict_row = res[i]
            df = df.append(dict_row, ignore_index=True)

        return df

    def get_week_candle(self, market='KRW-BTC', to=None, count=1) -> pd.DataFrame:
        """
        특정 화폐의 주봉 조회

        Parameters
        ----------
        market : string
            마켓 코드. 기본값은 KRW-BTC
        to : string
            마지막 캔들 시각(exclusive). 기본값은 None
            포맷 : yyyy-MM-dd HH:mm:ss
        count : int
            캔들 갯수. 기본값은 1. 최대 200개까지 요청 가능. 
        """

        df = pd.DataFrame()
        base_url = self.BASE_API_URL + '/candles/weeks?'

        if to:
            print(f'{market} => {to}보다 이전 주봉 데이터 조회')
            to = to.replace(' ', '%20').replace(':', '%3A')
            query = 'market={}&to={}&count={}'.format(market, to, count)
        else:
            query = 'market={}&count={}'.format(market, count)

        url = base_url + query

        # try - except
        res = rq.get(url, headers=self.headers).json()
        time.sleep(0.1)

        for i in range(len(res)):
            dict_row = res[i]
            df = df.append(dict_row, ignore_index=True)

        return df

    def get_month_candle(self, market='KRW-BTC', to=None, count=1) -> pd.DataFrame:
        """
        특정 화폐의 월봉 조회

        Parameters
        ----------
        market : string
            마켓 코드. 기본값은 KRW-BTC
        to : string
            마지막 캔들 시각(exclusive). 기본값은 None
            포맷 : yyyy-MM-dd HH:mm:ss
        count : int
            캔들 갯수. 기본값은 1. 최대 200개까지 요청 가능. 
        """

        df = pd.DataFrame()
        base_url = self.BASE_API_URL + '/candles/months?'

        if to:
            print(f'{market} => {to}보다 이전 월봉 데이터 조회')
            to = to.replace(' ', '%20').replace(':', '%3A')
            query = 'market={}&to={}&count={}'.format(market, to, count)
        else:
            query = 'market={}&count={}'.format(market, count)

        url = base_url + query

        # try - except
        res = rq.get(url, headers=self.headers).json()
        time.sleep(0.1)

        for i in range(len(res)):
            dict_row = res[i]
            df = df.append(dict_row, ignore_index=True)

        return df

    def get_transactions(self, market='KRW-BTC', to=None, count=1, cursor=None, days_ago=None):
        pass

    def get_ticker(self, market='KRW-BTC'):
        pass

    def get_orderbook(self, markets=['KRW-BTC']):

        df = pd.DataFrame()
        base_url = self.BASE_API_URL + '/orderbook?'

        if len(markets) > 1:
            params = '%2C%20'.join(markets)
            query = 'markets={}'.format(params)
        else:
            params = markets[0]
            query = 'markets={}'.format(params)

        url = base_url + query

        # try - except
        res = rq.get(url, headers=self.headers).json()
        time.sleep(0.1)

        for market_idx in range(len(res)):
            market_orderbook = res[market_idx]

            market = market_orderbook['market']
            timestamp = market_orderbook['timestamp']
            total_ask_size = market_orderbook['total_ask_size']
            total_bid_size = market_orderbook['total_bid_size']
            orderbook_units = market_orderbook['orderbook_units']

            temp_df = pd.DataFrame()

            for orderbook_units_idx in range(len(orderbook_units)):
                temp_df = temp_df.append(
                    orderbook_units[orderbook_units_idx], ignore_index=True)

            temp_df['market'] = market
            temp_df['timestamp'] = timestamp
            temp_df['total_ask_size'] = total_ask_size
            temp_df['total_bid_size'] = total_bid_size

            df = df.append(temp_df, ignore_index=True)
            df = df.reset_index(drop=True)

        return df

