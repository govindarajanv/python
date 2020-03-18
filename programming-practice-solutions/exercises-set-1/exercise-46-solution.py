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

def read_from_db():
    #This is lile selection using the mouse on an editor
    cursor.execute('SELECT * FROM stuffToPlot')
    #you have to fectch to perform action on the selected records

    #one way is commented below
    #data = cursor.fetchall()
    #print (data)

    #each row is a tuple
    for row in cursor.fetchall():
        print (row)


#create_table()
##data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

read_from_db()
cursor.close()
conn.close()

