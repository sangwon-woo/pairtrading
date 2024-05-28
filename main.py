import os
import datetime
import time
from upbit import QuotationAPI

if __name__ == "__main__":
    uapi = QuotationAPI()
    ret = uapi.get_market_code()

    ret.to_csv("market_code.csv", index=False)