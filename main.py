
import datetime
import time
import pandas as pd
from os import listdir
from os.path import isfile, join
from upbit import QuotationAPI

database = '/Volumes/E/data/upbit'

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

    # exist_files = [f for f in listdir(database) if isfile(join(database, f))]
    
    for code in krw_market_code:
        # if code + '.csv' in exist_files:
        #     print(code+'.csv is already done')
        #     continue    
        # krw_btc = krw_market_code[0]
        if code != 'KRW-AKT':
            continue
        start_datetime = "2024-01-01 00:00:00"
        last_datetime = "2023-01-01 00:00:00"
        unit_count = 200

        total_df = pd.DataFrame()

        total_df = pd.concat(
            [total_df, uapi.get_minute_candle(
                unit = 1,
                market = code,
                to = start_datetime,
                count = unit_count
            )]
        )

        next_datetime = start_datetime

        while to_datetime(last_datetime) < to_datetime(next_datetime):
            next_datetime = str(to_datetime(next_datetime) - datetime.timedelta(minutes = unit_count))
            temp_df = uapi.get_minute_candle(
                    unit = 1,
                    market = code,
                    to = next_datetime,
                    count = unit_count
                )
            total_df = pd.concat(
                [total_df, temp_df ]
            )
            if temp_df.shape[0] < 200:
                break

        # total_df.to_csv(f'/Volumes/E/data/upbit/{code}.csv', index=None)
        total_df.to_csv(f'{code}.csv', index=None)
    # print(total_df.info())