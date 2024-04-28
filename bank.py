import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100000, 999999)
        self.accounts[account_number] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transaction_history': [],
            'loan_taken': 0,
            'loan_count': 0
        }
        print("Account created successfully. Your account number is:", account_number)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Available balance:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist.")

    def transaction_history(self, account_number):
        if account_number in self.accounts:
            print("Transaction History:")
            for transaction in self.accounts[account_number]['transaction_history']:
                print(transaction)
        else:
            print("Account does not exist.")

    def total_balance(self):
        total = sum(acc['balance'] for acc in self.accounts.values())
        print("Total available balance in the bank:", total)

    def total_loan_amount(self):
        total = sum(acc['loan_taken'] for acc in self.accounts.values())
        print("Total loan amount in the bank:", total)

    def enable_loan_feature(self):
        self.loan_feature_enabled = True
        print("Loan feature has been enabled.")

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        print("Loan feature has been disabled.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['transaction_history'].append(f"Deposited: {amount}")
            print("Amount deposited successfully.")
        else:
            print("Account does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['transaction_history'].append(f"Withdrew: {amount}")
                print("Amount withdrawn successfully.")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Account does not exist.")

    def take_loan(self, account_number, amount):
        if account_number in self.accounts:
            if self.loan_feature_enabled:
                if self.accounts[account_number]['loan_count'] < 2:
                    self.accounts[account_number]['loan_taken'] += amount
                    self.accounts[account_number]['loan_count'] += 1
                    self.accounts[account_number]['balance'] += amount
                    self.accounts[account_number]['transaction_history'].append(f"Loan taken: {amount}")
                    print("Loan taken successfully.")
                else:
                    print("You have already taken maximum number of loans.")
            else:
                print("The loan feature is currently disabled by the admin.")
        else:
            print("Account does not exist.")

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number]['balance'] >= amount:
                self.accounts[from_account_number]['balance'] -= amount
                self.accounts[to_account_number]['balance'] += amount
                self.accounts[from_account_number]['transaction_history'].append(f"Transferred: {amount} to {to_account_number}")
                self.accounts[to_account_number]['transaction_history'].append(f"Received: {amount} from {from_account_number}")
                print("Amount transferred successfully.")
            else:
                print("Insufficient balance to transfer.")
        else:
            print("One or both of the accounts do not exist.")


