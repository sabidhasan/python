#This code declares a class called BankAccount. Within this class we then use the __init__ function to create a variable 'balance'.
#We also define three functions: 'withdraw', 'deposit' and 'display'.
#
#To improve upon this code moving forwards, I will incorperate a webscraping tool into this that takes live data from a currency
#conversion website. Then we can include functions within each of the already-present functions to allow for a currency of choice
#to be chosen.

class BankAccount(object):

    def __init__(self,balance=0.0):
        self.balance = balance

    def withdraw(self):
        withdraw_amount = float(input("How much money would you like to withdraw? "))
        while withdraw_amount > self.balance:
            print("Insufficient funds. Enter again. ")
        self.balance -= withdraw_amount
        print(f'Withdraw successful. You now have a balance of: {self.balance}')

    def deposit(self):
        deposit_amount = float(input("How much money would you like to deposit? "))
        self.balance += deposit_amount
        print(f'Deposit successful. You now have a balance of: {self.balance}')


    def display(self):
        print('Your bank account balance is {self.balance}.')

#Examples of how to call the functions of the class:
# my_bank = BankAccount(300)
# my_bank.withdraw()
# my_bank.deposit()
# mybank.display()
