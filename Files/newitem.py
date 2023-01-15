#!/usr/bin/python3

import sys
import os
import datetime
from easySqlite3 import Db

#VARS############################
now = datetime.datetime.now()
#Open Logfile
logfile = open('applog.txt', 'a')
sys.stdout = logfile
#################################
def additem():

    print("Clipam Logfile")
    print(now)





    TABLE = '''
            CREATE TABLE IF NOT EXISTS inventory(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Item TEXT NOT NULL,
            PartNumber TEXT NOT NULL,
            Quantity TEXT NOT NULL,
            Comments TEXT NULL
            );
            '''

    DATA_BASE_PATH = 'data/fiber.sql'
    #db = 'data/ipdb.sql'
    INSERT_QUERY = 'INSERT INTO inventory(Item, PartNumber, Quantity, Comments) VALUES (?, ?, ?, ?)'


    # start an data base object
    db = Db(DATA_BASE_PATH)

    # connect to the data base
    db.connect()

    # create the table
    db.createTable(TABLE)

    # prepare query
    db.prepareQuery(INSERT_QUERY)

    #        print('Clipam Help Menu')
    #        print("clipam <ip addr> <netmask> <hostname> <comment>")
    #        print("clipam 1.1.1.1 255.255.255.0 giga.ios.devicename CoreRouter")

    inv_item = sys.argv[1]
    inv_part = sys.argv[2]
    inv_count = sys.argv[3]
    inv_comment = sys.argv[4]

    print("Device Entry: ")
    print("   IP      NETMASK      DEVICE  ")
    print(inv_item + ' ' + inv_part + ' ' + inv_count)


    # insert into table
    db.insertRow([inv_item, inv_part, inv_count, inv_comment])

    # closing connection
    db.close()



    logfile.close()

if __name__ == '__main__':
    additem()
