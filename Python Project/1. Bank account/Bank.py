# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance

class Bank :
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debitted from your account")
        print("Total balance is Rs", self.get_balance())
   
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited in your account")
        print("Total balance is Rs", self.get_balance())
    
    #get balance method
    def get_balance(self):
        return self.balance



acc1 = Bank(256700, 9734974973)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(497)
acc1.credit(800)
acc1.get_balance()
