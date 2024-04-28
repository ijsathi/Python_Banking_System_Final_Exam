class User:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings or Current): ").capitalize()
        self.bank.create_account(name, email, address, account_type)

    def deposit(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount to deposit: "))
        self.bank.deposit(account_number, amount)

    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount to withdraw: "))
        self.bank.withdraw(account_number, amount)

    def check_balance(self):
        account_number = int(input("Enter your account number: "))
        self.bank.check_balance(account_number)

    def transaction_history(self):
        account_number = int(input("Enter your account number: "))
        self.bank.transaction_history(account_number)

    def take_loan(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter loan amount: "))
        self.bank.take_loan(account_number, amount)

    def transfer(self):
        from_account_number = int(input("Enter your account number: "))
        to_account_number = int(input("Enter recipient's account number: "))
        amount = float(input("Enter amount to transfer: "))
        self.bank.transfer(from_account_number, to_account_number, amount)