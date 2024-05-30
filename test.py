import pandas as pd
import numpy as np
from os import listdir
from os.path import getsize

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def check_dtypes(df):
    col_dtypes = {}
    list_int = ['int', 'int8', 'uint8', 'int16',
                'uint16', 'int32', 'uint32', 'int64', 'uint64']
    list_float = ['float', 'float32', 'float64']

    for col in df.columns:
        dtype = df[col].dtype

        if dtype in list_int or dtype in list_float:
            c_min = df[col].min()
            c_max = df[col].max()

            if dtype in list_int:
                if c_min >= np.iinfo(np.int8).min and c_max <= np.iinfo(np.int8).max:
                    col_dtype = 'int8'
                elif c_min >= np.iinfo(np.uint8).min and c_max <= np.iinfo(np.uint8).max:
                    col_dtype = 'uint8'
                elif c_min >= np.iinfo(np.int16).min and c_max <= np.iinfo(np.int16).max:
                    col_dtype = 'int16'
                elif c_min >= np.iinfo(np.uint16).min and c_max <= np.iinfo(np.uint16).max:
                    col_dtype = 'uint16'
                elif c_min >= np.iinfo(np.int32).min and c_max <= np.iinfo(np.int32).max:
                    col_dtype = 'int32'
                elif c_min >= np.iinfo(np.uint32).min and c_max <= np.iinfo(np.uint32).max:
                    col_dtype = 'uint32'
                elif c_min >= np.iinfo(np.int64).min and c_max <= np.iinfo(np.int64).max:
                    col_dtype = 'int64'
                elif c_min >= np.iinfo(np.uint64).min and c_max <= np.iinfo(np.uint64).max:
                    col_dtype = 'uint64'

            elif dtype in list_float:
                # if c_min >= np.finfo(np.float16).min and c_max <= np.finfo(np.float16).max:
                #     col_dtype = 'float16'
                if c_min >= np.finfo(np.float32).min and c_max <= np.finfo(np.float32).max:
                    col_dtype = 'float32'
                elif c_min >= np.finfo(np.float64).min and c_max <= np.finfo(np.float64).max:
                    col_dtype = 'float64'

        elif dtype == 'object':
            n_unique = df[col].nunique()
            threshold = n_unique / df.shape[0]

            if threshold > 0.7:
                col_dtype = 'object'
            else:
                col_dtype = 'category'

        elif dtype == 'category':
            col_dtype = dtype

        col_dtypes[col] = col_dtype

    return col_dtypes

def set_columns_dtypes(df):
    
    if df.columns[0] == '시장-코인':
        dtypes = self.check_dtypes(df)
        df = df.astype(dtypes)
        return df

    columns = {
        'market': '시장-코인',
        'candle_date_time_utc': '시각_utc',
        'candle_date_time_kst': '시각_kst',
        'opening_price': '시가',
        'high_price': '고가',
        'low_price': '저가',
        'trade_price': '종가',
        'candle_acc_trade_price': '누적거래금액',
        'candle_acc_trade_volume': '누적거래량'
    }
    df = df.drop(columns=['timestamp', 'unit']).rename(columns=columns)
    dtypes = check_dtypes(df)
    df = df.astype(dtypes)

    return df

# database = '.\\upbit'

# price_data = [database+'\\'+f for f in listdir(database)]
# for _dir in price_data:
#     print(_dir, end=' ')
#     print(convert_bytes(getsize(_dir)), end='=> ')
#     tdf = pd.read_csv(_dir, encoding='utf-8')
#     tdf = set_columns_dtypes(tdf)
#     tdf.to_csv(_dir, index=None, encoding='utf-8')
#     print(convert_bytes(getsize(_dir)))
