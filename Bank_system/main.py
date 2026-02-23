import json
import os
import random
import hashlib

def load_users():
    if not os.path.exists('users.json'):
        return {}

    with open('users.json', 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
    
def save_users(users):
    with open("users.json", 'w') as f:
        json.dump(users, f, indent=4)

def generate_id():
    return random.randint(10000, 99999)


def create_account():
    users = load_users()
    while True:
        username = input("Username (lowercase): ").lower()
        if username in users:
            print("Name already exists! Try again.")
            continue
        password = input("Password: ")
        account = {
            "id": generate_id(),
            "password": hash_password(password),
            "balance": 0
        }
        users[username] = account
        save_users(users)
        print("Account created successfully!")
        break

def login():
    accounts = load_users()
    while True:
        try:
            print("_"*50)
            get_username = input("Enter Username: ").lower()
            if get_username in accounts:
                while True:
                    try:
                        get_password = input("Enter Password: ")
                        if hash_password(get_password) == accounts[get_username]['password']:
                            print("Login successful.\n")
                            return get_username
                        else:
                            user = input("Wrong password (again => Enter | back => 'b'): ").lower()
                            if user == 'b':
                                break
                            continue
                    except ValueError:
                        print("Error!")
            else:
                print("Not Found!")
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)

def deposit(user):
    users = load_users()
    while True:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            users[str(user)]['balance'] += amount 
            save_users(users)
            print('Deposit successful!') 
            break
        elif amount <= 0:
            print("Error! Amount must be more than zero.")
            continue
        elif amount is not int():
            print("Error! Must be integar.")
            continue

def withdraw(user):
    users = load_users()
    while True:
        try:
            amount = int(input("Enter withdraw amount: "))
            if amount > 0:
                if amount <= users[user]['balance']:
                    users[user]['balance'] -= amount
                    save_users(users)
                    print('Withdraw Successfull!')
                    break
                else:
                    print("amount bigger than balance.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Please Enter the number.")
            
def view_balance(user):
    users = load_users()
    print(f"Username => {user} | Balance => {users[user]['balance']}")

def user_menu(user):
    while True:
        try:
            print("*" * 50)
            print("1. Deposit\n" \
            "2. Withdraw\n" \
            "3. View Balance\n" \
            "4. Logout")
            choose = input("> ")
            if choose == '1':
                deposit(user)
            elif choose == '2':
                withdraw(user)
            elif choose == '3':
                view_balance(user)
            elif choose == '4':
                print("Logging out...")
                break
            else:
                print("Choose '1', '2', '3', '4'.")
        except ValueError:
            print("Error! Try again.")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    while True:
        try:
            print("_"*50)
            print("1. Create Account\n" \
            "2. Login\n" \
            "3. Exit")
            user = input("> ")
            if user == '1':
                create_account()
            elif user == '2':
                user = login()
                if user:
                    user_menu(user)
            elif user == '3':
                print("Exit...")
                break
            else:
                print("Choose '1', '2', '3'.")
        except ValueError:
            print("Error! Try again.")

if __name__ == '__main__':
    main()