#!/usr/bin/python3

import sys
import os
import datetime
from easySqlite3 import Db



#VARS############################
path = os.getcwd()
now = datetime.datetime.now()
#Open Logfile
logfile = open('applog.txt', 'a')
sys.stdout = logfile
#################################
print("FiberInventory Logfile")
print(now)

#Create Directory
try:
    os.mkdir(path + '/data')
except OSError:
    print ("Directory Creation Has Failed For Directory: /data ")
else:
    print ("Directory Creation Was Successful For Directory: /data ")




#Create Database
print("Building Database: invdb.sql @: /data/ ")

TABLE = '''
        CREATE TABLE IF NOT EXISTS inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Item TEXT NOT NULL,
        PartNumber TEXT NOT NULL,
        Quantity TEXT NOT NULL,
        Location TEXT NOT NULL,
        Manufacturer TEXT NULL
        );
        '''

DATA_BASE_PATH = 'data/invdb.sql'

db = Db(DATA_BASE_PATH)

db.connect()

#Close Database
db.close()

#Close Logfile
logfile.close()






