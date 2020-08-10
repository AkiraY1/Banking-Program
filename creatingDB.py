import sqlite3

conn = sqlite3.connect('customers.db')
cur = conn.cursor()

cur.execute('CREATE TABLE customers(username TEXT PRIMARY KEY, name TEXT, password TEXT, balance INT);')
conn.commit()