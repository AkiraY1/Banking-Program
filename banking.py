import sqlite3
import time
from account import Account

# Admin account:
# Username: Admin
# Name: Admino
# Password: password

def dashboard(a):
    theName = a.get_name()
    theBalance = a.get_balance()
    print('-----------------------------------------------------------------------------------------------')
    print(f"{theName}'s DASHBOARD")
    print(f"Balance: {theBalance}" + '\n')
    print("Instructions:")
    print("Deposit money (Deposit [amount]), Withdraw money (withdraw [amount]), Logout (l)")
    dashChoice = input()
    if dashChoice == 'r':
        dashboard(a)
    if dashChoice == 'l':
        print("Logging out...")
        time.sleep(2)
        welcomePage()
    if dashChoice.split()[0] == 'Deposit':
        money = dashChoice.split()[1]
        a.deposit(theName, theBalance, money)
        print("Deposited successfully")
        print("Now redirecting to your account dashboard...")
        dashboard(a)
    if dashChoice.split()[0] == 'Withdraw':
        money = dashChoice.split()[1]
        a.withdraw(theName, theBalance, money)
        print("Withdrawn successfully")
        print("Now redirecting to your account dashboard...")
        dashboard(a)
    else:
        print("I'm sorry, you need to enter any of the commands above. Your page will now reload.")
        time.sleep(2)
        dashboard(a)

def loginPage():
    print('-----------------------------------------------------------------------------------------------')
    print('LOGIN PAGE')
    print('[If you ever want to reload the signup page, enter r for any of the following questions]')
    username = input("Username: ")
    if username == 'r':
        loginPage()
    password = input("Password: ")
    if password == 'r':
        loginPage()
    balance = 0
    name = None
    a = Account(name, username, password, balance)
    verification = a.verify_account()
    if verification:
        print("Logged in successfully")
        print("Now redirecting to your account dashboard...")
        time.sleep(2)
        dashboard(a)
    else:
        print("Incorrect. Reloading the page...")
        time.sleep(2)
        loginPage()

def welcomePage():
    print('-----------------------------------------------------------------------------------------------')
    print("Welcome to the Akira Bank!")
    print("Any time that you want to reload a page (which can only be done when given an input option), type 'r' and press enter")
    print("You can either login [1] or create an account [2]")
    welcomeChoice = input()
    if welcomeChoice.strip() == '1':
        loginPage()
    elif welcomeChoice.strip() == '2':
        signupPage()
    elif welcomeChoice.strip() == 'r':
        welcomePage()
    else:
        print("I'm sorry, you need to enter either 1, 2 or r. Your page will now reload.")
        time.sleep(2)
        welcomePage()

def signupPage():
    print('-----------------------------------------------------------------------------------------------')
    print("SIGNUP PAGE")
    print('[If you ever want to leave the signup page, enter l for any of the following questions]')
    print('[If you ever want to reload the signup page, enter r for any of the following questions]')
    name = input('Name: ')
    if name == 'l':
        welcomePage()
    if name == 'r':
        signupPage()
    username = input('Username: ')
    if username == 'l':
        welcomePage()
    if username == 'r':
        signupPage()
    password = input('Password: ')
    if password == 'l':
        welcomePage()
    if password == 'r':
        signupPage()
    a = Account(name, username, password, balance=0)
    a.create_account()
    print("Successful! Transporting to account dashboard...")
    time.sleep(2)
    dashboard(a)

welcomePage()