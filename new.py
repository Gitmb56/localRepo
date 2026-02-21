class BankAccount:
    def __init__(self):
        self.name = "Mangal Baski"
        self.  __balance = 0                # Mangled this private

    def Deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit amount {self.__balance}")

    def withdraw(self,amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdraw amount {self.__balance}")

    def show(self):
        print(f"Account Holder {self.name} \n Balance : {self.__balance}") 

# Object Creation

a1 = BankAccount()
user_in = int(input("Enter Deposit amount: "))
a1.Deposit(user_in)
a1.show()
#print(a1.__dict__)