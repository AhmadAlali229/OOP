class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance



account = BankAccount("Ahmad", 1000)

account.deposit(500)
print(account.get_balance())  


print(account.get_balance()) 
         