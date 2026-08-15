from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance


    @property
    def balance(self):
        return self._Account__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount 

    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance+= amount

    @abstractmethod
    def withdraw(self, amount):
        pass


    def __str__(self):
        return f"Account({self.account_number}) Balance = {self.balance}"

    

class SavingsAccount(Account):

    minBalance = 1000

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.minBalance =  SavingsAccount.minBalance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Don't have amount to withdraw ")
        elif (self.balance - amount ) < self.minBalance:
            raise ValueError(f"Account needs minimum balance of {self.minBalance}")
        else:
            self.balance -= amount

class CurrentAccount(Account):

    overdraft_limit = 500

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.overdraft_limit = CurrentAccount.overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Don't have amount to withdraw ")
        elif ( self.balance - amount ) < -self.overdraft_limit:
            raise ValueError(f"Account has overdraft limit of {self.overdraft_limit} only, can't withdraw above that amount")
        else:
            self.balance-= amount



class Customer:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, Account):
        self.accounts.append(Account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)




class Bank:

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, Customer):
        self.customers.append(Customer)

    def total_deposit(self):
        return sum( c.total_balance() for c in self.customers)
