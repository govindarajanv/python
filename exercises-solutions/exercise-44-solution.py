# SQLite Exercises

import sqlite3

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

create_table()
data_entry()
