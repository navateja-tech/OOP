class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner              
        self.__balance = balance 

    @property
    def balance(self) -> float:
        """Getter: allows reading the balance safely."""
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"[{self.owner}] Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            print(f"[{self.owner}] Insufficient funds!")
            return
        self.__balance -= amount
        print(f"[{self.owner}] Withdrew {amount}. New balance: {self.__balance}")



if __name__ == "__main__":
    account = BankAccount("Teja", 1000.0)

    account.deposit(500)
    account.withdraw(300)
    print("Current balance:", account.balance)

    try:
        print(account.__balance)
    except AttributeError as e:
        print("Direct access blocked:", e)

    print("Accessed via name mangling:", account._BankAccount__balance)

    account.balance = 2000
    print("Balance after direct property set:", account.balance)

    try:
        account.balance = -100
    except ValueError as e:
        print("Validation caught it:", e)