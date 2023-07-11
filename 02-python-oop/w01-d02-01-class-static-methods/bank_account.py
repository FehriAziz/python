class BankAccount:
    all_accounts = []
    
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.02, balance=0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        
        return self
        # print (mohamed.balance)


    def withdraw(self, amount):
        self.balance -= amount
    

        return self
        # print(mohamed.withdraw)

    def display_account_info(self):
        print(f"your int-rate ={self.int_rate} , and your balance is {self.balance}")
        return self
    

    def yield_interest(self ):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        # print(self.balance*self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    





mohamed = BankAccount(0.2 , 50)
ali = BankAccount(0.5,500)
mohamed.deposit(20).deposit(10).deposit(1000).withdraw(150)
# mohamed.withdraw(150)
# mohamed.display_account_info()
mohamed.yield_interest()

# client1 = BankAccount()
# client1.deposit(50).withdraw(10).display_account_info().yield_interest().display_account_info()
BankAccount.print_all_accounts()