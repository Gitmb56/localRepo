class BankAccount:
    def __init__(self, owner='Mangal', initial_balance=0):
        self.owner = owner
        self._balance = initial_balance          # protected by convention
        # self.__balance = initial_balance       # name mangled (strong hint)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            raise ValueError("Invalid withdrawal amount")

    @property
    def balance(self):          # read-only view
        return self._balance