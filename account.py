import sqlite3
import time

conn = sqlite3.connect('customers.db')
cur = conn.cursor()

class Account():
    def __init__(self, name, username, password, balance):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance
    
    def create_account(self):
        person = (self.username, self.name, self.password, self.balance)
        cur.execute("INSERT INTO customers VALUES(?, ?, ?, ?);", person)
        conn.commit()
   
    def verify_account(self):
        cur.execute(f"SELECT * FROM customers WHERE username = '{self.username}';")
        results = cur.fetchall()
        if results == []:
            return False
        if results[0][0] == self.username:
            if results[0][2] == self.password:
                return True
            else:
                return False
        else:
            return False

    def get_name(self):
        cur.execute(f"SELECT * FROM customers WHERE username = '{self.username}';")
        results = cur.fetchall()
        theName = results[0][1]
        return theName
        
    def get_balance(self):
        cur.execute(f"SELECT * FROM customers WHERE username = '{self.username}';")
        results = cur.fetchall()
        theBalance = results[0][3]
        return theBalance
    
    def deposit(self, theName, theBalance, money):
        updatedBalance = int(theBalance) + int(money)
        cur.execute(f"UPDATE customers set balance = {updatedBalance} where name = '{theName}';")
        conn.commit()
    
    def withdraw(self, theName, theBalance, money):
        updatedBalance = int(theBalance) - int(money)
        cur.execute(f"UPDATE customers set balance = {updatedBalance} where name = '{theName}';")
        conn.commit()
