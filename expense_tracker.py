# personal expense tracker 

import getpass
import os
import re
from datetime import datetime

# credentials file and master password

CREDENTIALS_FILE = "data/credentials.txt"
MASTER_PASSWORD = "root"


def authenticate_user():
    if not os.path.exists(CREDENTIALS_FILE):
        print("No credentials found. Let's set it up.")
        username = input("Create username: ")
        password = getpass.getpass("Create password: ")

        with open(CREDENTIALS_FILE, "w") as f:
            f.write(f"{username}:{password}")
        print("Setup complete. Please login to continue.")
        return authenticate_user()

    with open(CREDENTIALS_FILE, "r") as f:
        cred = f.read().strip().split(":")

    for _ in range(3):
        username = input("Username: ")
        password = getpass.getpass("Password: ")


        if username == cred[0] and password == cred[1]:
            print("Login successful!")
            return True
        else:
            print("Wrong credentials. Try again.")

    print("Too many failed attempts.")
    return False


def change_password():
    master = getpass.getpass("Enter master password to proceed: ")
    if master != MASTER_PASSWORD:
       print("Wrong master password!")
       return

    new_username = input("Enter new username: ")
    new_password = getpass.getpass("Enter new password: ")

    with open(CREDENTIALS_FILE, "w") as f:
        f.write(f"{new_username}:{new_password}")
    print("Username and password changed successfully!")



def validate_format(date):
    pattern = r"^\d{2}-\d{2}-\d{4}$"
    if re.match(pattern, date):
        return True
    else:
        return False




def add_expense():
    while True:
        date = input("Enter Date (DD-MM-YYYY): ")
        
        if validate_format(date):
            break
        else:
            print("Invalid date format. Please use DD-MM-YYYY format.")

    category = input("Enter category (e.g., Food, Transport): ")
    amount = int(input("Enter Amount: "))

    with open('data/expense.txt', 'a') as file:
        file.write(f"{date} | {category} | ₹ {amount}\n")

    print("Expense added successfully!")




def view_expense():
    try:
        with open('data/expense.txt', 'r') as file:
            expenses = file.readlines()
            if not expenses:
                print("No expense recorded yet.")
            else:
                expenses.sort(key=lambda x: datetime.strptime(x.split(' | ')[0], "%d-%m-%Y") )

                print("==== Expenses ==== ")
                print("DATE | CATEGORY | AMOUNT")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.strip()}")
    except FileNotFoundError:
        print("No expenses file found. Add some expenses first.")



def remove_expense():
    try:
        with open('data/expense.txt', 'r') as file:
            expenses = file.readlines()

        if not expenses:
           print("No expenses to delete.")
           return

        print("===== Expenses =====")
        expenses.sort(key=lambda x: datetime.strptime(x.split(' | ')[0], "%d-%m-%Y") )
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense.strip()}")

        choice = input("Enter the number of the expense to remove: ")

        try:
            choice = int(choice)
            if choice < 1 or choice > len(expenses):
                print("Invalid choice. Please try again.")
                return
            else:
                removed_expense = expenses.pop(choice - 1)

            with open('data/expense.txt', 'w') as file:
                file.writelines(expenses)

            print(f"Expense '{removed_expense.strip()}' removed successfully!")

        except ValueError:
            print("Invalid input. Please enter a number.")

    except FileNotFoundError:
        print("No expense file found. Add some expeneses first.")

    


def show():
    print("----- Personal Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Remove Expenses")
    print("4. Change Username/Password")
    print("5. Exit")



def main():
    if not authenticate_user():
        return


    while True:
        show()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            remove_expense()
        elif choice == '4':
            change_password()
        elif choice == '5':
            print("Exting ....")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()

