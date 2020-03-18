# SQLite Exercises

import sqlite3
import datetime
import time
import random

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

#convention is to capitalize SQL statements and programming in regular case
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, date TEXT, keyword TEXT, value REAL)')


def data_entry():
    cursor.execute("INSERT INTO stuffToPlot VALUES(53456234,'2016-02-01', 'Django',6)")
    conn.commit()
    cursor.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    cursor.execute("INSERT INTO stuffToPlot (unix,date, keyword,value) VALUES(?,?, ?,?)",(unix,date,keyword,value))
    conn.commit()

create_table()
#data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

cursor.close()
conn.close()

