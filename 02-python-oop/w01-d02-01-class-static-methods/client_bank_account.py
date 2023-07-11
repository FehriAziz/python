class User:
    multi_account = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def make_account(self, int_rate, balance, id):
        new_account = BankAccount(int_rate, balance, id)
        self.multi_account.append(new_account)

    def make_deposit(self, account_id, amount):
        account = self.find_account(account_id)
        if account:
            account.deposit(amount)
        else:
            print("Account not found")

    def make_withdrawal(self, account_id, amount):
        account = self.find_account(account_id)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found")

    def display_user_balance(self, account_id):
        account = self.find_account(account_id)
        if account:
            print(f"You have {account.balance} in account {account.id}")
        else:
            print("Account not found")

    def find_account(self, account_id):
        for account in self.multi_account:
            if account.id == account_id:
                return account
        return None


class BankAccount:
    def __init__(self, int_rate, balance, id):
        self.int_rate = int_rate
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


user = User("John Doe", "john@gmail.com")
user.make_account(0.02, 500, 1)
user.make_account(0.1, 100, 2)

user.make_deposit(1, 100) 
user.make_withdrawal(2, 50) 

user.display_user_balance(1)  
user.display_user_balance(2)  
user.display_user_balance(3)  