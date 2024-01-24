class BankAccount :

    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self,amount):
        print("The amount in your account prior to deposit is :" , self.balance)
        self.balance +=amount
        print("The amount in your account later the deposit is :" , self.balance)

    def withdraw(self,amount):
        print("The amount in your account before withdraw is :" , self.balance)
        self.balance -= amount
        print("The amount in your account is :" , self.balance)
bank = BankAccount(0,501)
bank.deposit(3000)
bank.withdraw(2000)