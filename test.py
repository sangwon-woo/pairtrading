
database = '/Volumes/E/data/upbit'
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(database) if isfile(join(database, f))]
print(onlyfiles)