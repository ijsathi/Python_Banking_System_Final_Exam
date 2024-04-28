class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self):
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        address = input("Enter user's address: ")
        account_type = input("Enter account type (Savings or Current): ").capitalize()
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self):
        account_number = int(input("Enter account number to delete: "))
        self.bank.delete_account(account_number)

    def see_all_accounts(self):
        print("All User Accounts:")
        for account_number, details in self.bank.accounts.items():
            print(f"Account Number: {account_number}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Account Type: {details['account_type']}")

    def total_available_balance(self):
        self.bank.total_balance()

    def total_loan_amount(self):
        self.bank.total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()