# -------------------------MINI PROJECT NO.1------------------------

# --------------------Create a simple ATM system---------------

class ATM:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print("Available Balance:",self.balance)    
            
    def deposit(self,amount):
        if amount > 0:
            self.balance +=amount
            print("Deposit successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
                print("Invalid withdrawal amount")
        elif amount > self.balance:
                print("Insufficient balance")
        else:
                self.balance -= amount
                print("Withdrawal successful")            

atm =ATM("Amit", 1000)   
atm.check_balance()
atm.deposit(2000)
atm.withdraw(3000)
atm.check_balance()         