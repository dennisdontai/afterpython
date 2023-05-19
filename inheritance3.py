class BankAccount:
    balance = True#attribute
    def deposit(self):
        print("Need some money")

    def withdraw(self):
        print("I borrowed a couple")

    def checkBalance(self):
        print("Fifty thousand in my account")

    def transfer(self):
        print("I transferred about fifty thousand pounds")


class InterestAccount(BankAccount):
    def interest(self):
        print("We had a massive increase in the number of sales")

    def deposit(self):
       print("Same as the withdrawn amount")

class ChargingAccount(BankAccount):
    def fee(self):
        print("As soon as we paid the fee we knew it was done")

    def withdraw(self):
        print("Same as the deposited")


rest = InterestAccount()
rest.deposit()
rest.withdraw()
rest.checkBalance()
rest.transfer()

prop = InterestAccount()
prop.interest()
prop.deposit()

charge = ChargingAccount()
charge.fee()
charge.withdraw()



