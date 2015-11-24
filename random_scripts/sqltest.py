#!/usr/bin/python3
import sqlite3
conDB = sqlite3.connect("/root/Desktop/python/random_scripts/test.db")
cDB = conDB.cursor()
cDB.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')
cDB.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conDB.commit()
conDB.close()