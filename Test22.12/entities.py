from errors import *
from random import randint


class Bank:
    def __init__(self):
        self.users = []
        self.accounts = []

    def add_user(self, names, egn):
        if len(names) < 4:
            raise InvalidDataFormat("Incorrect length name")
        for i in names:
            if i.isnumeric() or i.isalpha() or i == " ":
                pass
            else:
                raise InvalidDataFormat("Incorrect name")
        if len(egn) != 10 or not egn.isnumeric():
            raise InvalidDataFormat("Incorrect egn")
        user = User(names, egn)
        self.users.append(user)

    def add_account(self, egn, balance, currency, acc_type):
        for i in self.users:
            if i[1] == egn:
                if type(balance) != float:
                    raise InvalidDataFormat("Balance must be float number")
                if currency != "BGN" or currency != "EUR" or currency != "USD" or currency != "JPY":
                    raise InvalidAccCurrency("Invalid account currency")
                if acc_type != "CURRENT" or acc_type != "SAVINGS" or acc_type != "CREDIT":
                    raise InvalidAccType("Invalid account type")
                acc = Account(balance, currency, acc_type)
                egn.account.append(acc)
                break
        raise UserNotFound("Invalid EGN")

    def print_users(self):
        print(self.users)


class User:
    def __init__(self,  names, egn):
        self.account = []
        self.names = names
        self.egn = int(egn)


class Account:
    def __init__(self, balance, currency, acc_type):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        iban_digits = ""
        for i in range(10):
            iban_digits += str(randint(1,9))
        self.iban = "BG9812" + iban_digits
