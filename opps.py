class BankAccount:
    """
    Docstring for BankAccount
    Here are private some details and which method use Encapsulataion
    and some techniques mangled
    """
    def __init__(self):
        self.__name = " Mangal"                             # Mangaled name ( Private this name)
        self.__balance = 0
    
    ###################################
    #     I deposit amount this account
    ###################################
    
    def deposit(self, amount:int):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount: {amount}")
    
    # withdraw amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"withdrawn amount: {amount}")
        else:
            print("Insufficient balance")

    def show_details(self):
        print(f"Account Holder name : {self.__name}")
        print(f"Bank Balance: {self.__balance}")

ac1 = BankAccount()
user_in = int(input("Enter your amount: "))
ac1.deposit(user_in)
ac1.withdraw(int(input("Enter your amount to withdraw: ")))
print( f"Account Details: {ac1.show_details()}")
