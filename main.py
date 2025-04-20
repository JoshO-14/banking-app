
from bank_account import BankAccount

print("Welcome to Joshua's Bank!")

create_account = input("Do you want to create a new account? (yes/no): ").strip().lower()
if create_account == 'yes':
    user_id = input("Enter a user ID: ")
    password = input("Enter a password for your account: ")
    account = BankAccount(user_id)
    account.create_account(password)
    print("Account created successfully!")
elif create_account == 'no':
    login_user = input("Do you want to log in? (yes/no): ").strip().lower()
    if login_user == 'yes':
        user_id = input("Enter your user ID: ")
        password = input("Enter your password: ")
        account = BankAccount(user_id)
        if not account.verify_password(password):
            print("Invalid user ID or password.")
            exit()
        else:
            account.create_account(password)
            print("Login successful!")
        # Check if account exists and password is correct
        if account.get_balance() is None:
            print("Invalid user ID or password.")
            exit()
    elif login_user == 'no':
        print("Exiting...")
        exit()

#account = BankAccount(user_id)
account.transaction_table()


while True:
    
    print("\nWhere would you like to navigate? Choose an option:")
    print("1. Check Account Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == '1':
        print("Your balance is:", account.get_balance())
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '4':
        delete_option = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
        if delete_option == 'yes':
            account.delete_account()
            print("Account deleted successfully.")
            break
        else:
            print("Account deletion cancelled.")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")