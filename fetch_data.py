import configparser

parser = configparser.ConfigParser()
parser.read('config/config.ini')

UPBIT_ACCESS_KEY = parser.get('upbit', 'access_key')
UPBIT_SECRET_KEY = parser.get('upbit', 'secret_key')
DIR_UPBIT_DATABASE = 'D:\\coin_database\\domestic\\upbit'
DIR_UPBIT_DAILY_CANDLE = DIR_UPBIT_DATABASE + '\\daily'
DIR_UPBIT_MINUTELY_CANDLE = DIR_UPBIT_DATABASE + '\\minutely'
DIR_UPBIT_DATABASE_BACKUP = 'E:\\backup\\coin_database\\domestic\\upbit'
DIR_UPBIT_DAILY_CANDLE_BACKUP = DIR_UPBIT_DATABASE_BACKUP + '\\daily'
DIR_UPBIT_MINUTELY_CANDLE_BACKUP = DIR_UPBIT_DATABASE_BACKUP + '\\minutely'