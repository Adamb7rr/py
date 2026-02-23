import string
import random

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError("Password length is too short for selected options.")
    
    password = ''
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def get_lenght():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError("Should be more than zero.")
            return length
        except ValueError as e:
            print(e)

def get_yes_no(prompt):
    while True:
        user = input(f"Include {prompt}? (y/n): ").lower()
        if user == 'y':
            return True
        elif user == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("Welcome to password generate")
    while True:
        user = input("\n1-generate 2-Exit: ")
        if user == '1':
            try:
                length = get_lenght()
                include_uppercase = get_yes_no("uppercase")
                include_numbers = get_yes_no("numbers")
                include_special = get_yes_no("special")
                password = generate_password(length, include_uppercase, include_numbers, include_special)
                print(f"\nGenerated password: {password}")
            except ValueError as e:
                print(e)
        elif user == '2':
            print("Exit...")
            break
        else:
            print("choose 1 or 2.")

if __name__ == '__main__':
    main()