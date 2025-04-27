import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image
from bank_account import BankAccount

# Create the main window
window = tk.Tk()
window.title("Joshua's Banking App")
window.geometry("800x500")
window.resizable(False, False)

# Image background
image_path = r"C:\Users\titil\Downloads\DOWNLOAD (2).JPG"
image = Image.open(image_path)
image = image.resize((800, 500), Image.Resampling.LANCZOS)  # Resize the image to fit the window
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add grid configuration
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Create a label widget
label = tk.Label(window, text="Welcome to Joshua's Bank!", font=("Times New Roman", 22))
label.grid(row=0, columnspan=2, pady=20)

# User ID Entry
userNameLabel = tk.Label(window, text="Enter Your User ID", font=("Times New Roman", 16))
userNameLabel.grid(row=1, column=0, padx=10, pady=10)

userName = tk.Entry(window, font=("Times New Roman", 16))
userName.grid(row=1, column=1, padx=10, pady=10)

# Password Entry
passwordLabel = tk.Label(window, text="Enter Your Password", font=("Times New Roman", 16))
passwordLabel.grid(row=2, column=0, padx=10, pady=10)

passwordEntry = tk.Entry(window, show="*", font=("Times New Roman", 16))
passwordEntry.grid(row=2, column=1, padx=10, pady=10)

# Define transaction menu
def transaction_menu(account):
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Transaction Menu", font=("Times New Roman", 22))
    label.grid(row=0, columnspan=2, pady=20)

    deposit_button = tk.Button(window, text="Deposit", command=lambda: deposit(account), font=("Times New Roman", 16))
    deposit_button.grid(row=1, column=0, padx=10, pady=10)

    withdraw_button = tk.Button(window, text="Withdraw", command=lambda: withdraw(account), font=("Times New Roman", 16))
    withdraw_button.grid(row=1, column=1, padx=10, pady=10)

    balance_button = tk.Button(window, text="View Balance", command=lambda: view_balance(account), font=("Times New Roman", 16))
    balance_button.grid(row=2, columnspan=2, pady=10)

    delete_account_button = tk.Button(window, text="Delete Account", command=lambda: delete_account(account), font=("Times New Roman", 16))
    delete_account_button.grid(row=3, columnspan=2, pady=10)

    exit_button = tk.Button(window, text="Exit", command=exit_app, font=("Times New Roman", 16))
    exit_button.grid(row=4, columnspan=2, pady=10)

# Define deposit function
def deposit(account):
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Deposit Money", font=("Times New Roman", 22))
    label.grid(row=0, columnspan=2, pady=20)

    amount_label = tk.Label(window, text="Enter Amount:", font=("Times New Roman", 16))
    amount_label.grid(row=1, column=0, padx=10, pady=10)

    amount_entry = tk.Entry(window, font=("Times New Roman", 16))
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    def confirm_deposit():
        amount = float(amount_entry.get())
        account.deposit(amount)

        print(f"Deposited {amount} successfully!")
        transaction_menu(account)

    confirm_button = tk.Button(window, text="Confirm", command=confirm_deposit, font=("Times New Roman", 16))
    confirm_button.grid(row=2, columnspan=2, pady=10)

# Define withdraw function
def withdraw(account):
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Withdraw Money", font=("Times New Roman", 22))
    label.grid(row=0, columnspan=2, pady=20)

    amount_label = tk.Label(window, text="Enter Amount:", font=("Times New Roman", 16))
    amount_label.grid(row=1, column=0, padx=10, pady=10)

    amount_entry = tk.Entry(window, font=("Times New Roman", 16))
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    def confirm_withdraw():
        amount = float(amount_entry.get())
        if amount > account.get_balance():
            print("Insufficient funds.")
        else:
            account.withdraw(amount)
            print(f"Withdrew {amount} successfully!")
            transaction_menu(account)

    confirm_button = tk.Button(window, text="Confirm", command=confirm_withdraw, font=("Times New Roman", 16))
    confirm_button.grid(row=2, columnspan=2, pady=10)

def delete_account(account):
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Delete Account", font=("Times New Roman", 22))
    label.grid(row=0, columnspan=2, pady=20)

    def confirm_delete():
        account.delete_account()
        print("Account deleted successfully!")
        window.destroy()

    confirm_button = tk.Button(window, text="Confirm", command=confirm_delete, font=("Times New Roman", 16))
    confirm_button.grid(row=1, columnspan=2, pady=10)

# Define view balance function
def view_balance(account):
    for widget in window.winfo_children():
        widget.destroy()

    balance = account.get_balance()
    label = tk.Label(window, text=f"Your Balance: ${balance:.2f}", font=("Times New Roman", 22))
    label.grid(row=0, columnspan=2, pady=20)

    back_button = tk.Button(window, text="Back", command=lambda: transaction_menu(account), font=("Times New Roman", 16))
    back_button.grid(row=1, columnspan=2, pady=10)

def exit_app():
    window.destroy()

# Define login function
def login():
    user_id = userName.get()
    password = passwordEntry.get()
    account = BankAccount(user_id, password)
    
    if account.verify_password(password):
        print("Login successful!")
        transaction_menu(account)
    else:
        print("Invalid credentials. Please try again.")

# Define signup function
def signup():
    user_id = userName.get()
    password = passwordEntry.get()
    account = BankAccount(user_id, password)
    
    try:
        account.create_account(password)
        print("Account created successfully!")
    except Exception as e:
        print(f"Error creating account: {e}")

# Create buttons
login_button = tk.Button(window, text="Login", command=login, font=("Times New Roman", 16))
signup_button = tk.Button(window, text="Sign Up", command=signup, font=("Times New Roman", 16))

# Add buttons to the window
login_button.grid(row=3, column=0, padx=10, pady=10)
signup_button.grid(row=3, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()