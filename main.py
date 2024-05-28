import os
import datetime
import time
import pandas as pd
from upbit import QuotationAPI

if __name__ == "__main__":
    uapi = QuotationAPI()

    # ret = uapi.get_market_code()
    # ret.to_csv("market_code.csv", index=False)
    # market_code = pd.read_csv("market_code.csv")
    # krw_code = [code for code in market_code['market'].to_list() if code.startswith('KRW')]
    # krw_market_code = market_code.loc[market_code['market'].isin(krw_code),]
    # krw_market_code.to_csv('krw_market_code.csv', index=False)

    