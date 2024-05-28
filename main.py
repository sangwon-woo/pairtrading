import os
import datetime
import time
import pandas as pd
from upbit import QuotationAPI

def to_datetime(str_datetime):
    _date, _time = str_datetime.split(' ')
    _year, _month, _day = map(int, _date.split('-'))
    _hour, _minute, _second = map(int, _time.split(':'))
    current_datetime = datetime.datetime(_year, _month, _day, _hour, _minute, _second)

    return current_datetime

if __name__ == "__main__":

    start_time = time.time()


    uapi = QuotationAPI()

    # ret = uapi.get_market_code()
    # ret.to_csv("market_code.csv", index=False)
    # market_code = pd.read_csv("market_code.csv")
    # krw_code = [code for code in market_code['market'].to_list() if code.startswith('KRW')]
    # krw_market_code = market_code.loc[market_code['market'].isin(krw_code),]
    # krw_market_code.to_csv('krw_market_code.csv', index=False)

    krw_market_code = pd.read_csv("krw_market_code.csv")
    krw_market_code = krw_market_code['market'].to_list()
    krw_btc = krw_market_code[0]

    start_datetime = "2017-09-25 03:01:00"
    unit_count = 200

    total_df = pd.DataFrame()

    total_df = pd.concat(
        [total_df, uapi.get_minute_candle(
            unit = 1,
            market = krw_btc,
            to = start_datetime,
            count = unit_count
        )]
    )
    print(total_df)
    # cnt = 0
    # next_datetime = start_datetime

    # while cnt < 10:
    #     next_datetime = str(to_datetime(next_datetime) - datetime.timedelta(minutes = unit_count))
    #     total_df = pd.concat(
    #         [total_df, uapi.get_minute_candle(
    #             unit = 1,
    #             market = krw_btc,
    #             to = next_datetime,
    #             count = unit_count
    #         )]
    #     )
    #     cnt += 1
    
    # print(total_df.info())