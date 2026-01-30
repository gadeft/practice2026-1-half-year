"""
Завдання 5. Реалізувати клас BankAccount із приватним атрибутом __balance,
методами deposit(amount) і withdraw(amount) та публічним методом get_balance() для
перегляду стану рахунку. Продемонструвати, як інкапсуляція захищає дані від прямої
зміни ззовні.
"""

class BankAccount:
    def __init__(self, balance, deposit):
        self.__balance = balance
        self.__deposit = deposit

    def __str__(self):
        sep = "\n------------------------\n"
        return sep + f"Balance: {self.__balance} \nDeposit: {self.__deposit}" + sep

    def get_balance(self):
        return self.__balance
    def get_deposit(self):
        return self.__deposit

    def deposit(self, amount):
        self.__deposit += amount
        self.__balance -= amount
    def withdraw(self, amount):
        self.__deposit -= amount
        self.__balance += amount


account = BankAccount(50000, 10000)
print(f"Balance: {account.get_balance()}")
print(f"Deposit: {account.get_deposit()}")
account.deposit(10000)
print(account)
account.withdraw(10000)
print(account)

# Data concealment
print(account.__balance)
print(account._BankAccount__balance)