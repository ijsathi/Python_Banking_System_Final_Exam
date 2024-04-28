from bank import Bank
from user import User
from admin import Admin

bank = Bank()
admin = Admin(bank)
user = User(bank)

while True:
    print("\nWelcome to the Bank System:")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nUser Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Transfer")
        print("8. Back to Main Menu")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            user.create_account()
        elif user_choice == '2':
            user.deposit()
        elif user_choice == '3':
            user.withdraw()
        elif user_choice == '4':
            user.check_balance()
        elif user_choice == '5':
            user.transaction_history()
        elif user_choice == '6':
            user.take_loan()
        elif user_choice == '7':
            user.transfer()
        elif user_choice == '8':
            continue
        else:
            print("Invalid choice.")

    elif choice == '2':
        print("\nAdmin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See All User Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Enable Loan Feature")
        print("7. Disable Loan Feature")
        print("8. Back to Main Menu")

        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            admin.create_account()
        elif admin_choice == '2':
            admin.delete_account()
        elif admin_choice == '3':
            admin.see_all_accounts()
        elif admin_choice == '4':
            admin.total_available_balance()
        elif admin_choice == '5':
            admin.total_loan_amount()
        elif admin_choice == '6':
            admin.enable_loan_feature()
        elif admin_choice == '7':
            admin.disable_loan_feature()
        elif admin_choice == '8':
            continue
        else:
            print("Invalid choice.")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice.")
