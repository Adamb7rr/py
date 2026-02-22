class ATM:
    def __init__(self):
        self.balance = 0
        self.history = []

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount less than balance.")
        self.balance += amount
        self.history.append(f"deposit ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be positive.")
        if amount > self.balance:
            raise ValueError("Amount should be less than balance.")
        self.balance -= amount
        self.history.append(f"withdraw ${amount}")
    
    def check_history(self):
        return self.history

class ATMController:
    def __init__(self):
        self.atm = ATM()

    def get_number(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("Enter Valid number.")
        
    def display_menu(self):
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. history")
        print("5. Exit")

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f"Balance: ${balance}")

    def deposit(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to deposit: ")
                self.atm.deposit(amount)
                print(f"Success! deposited ${amount}")
                break
            except ValueError as e:
                print(e)

    def withdraw(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to withdraw: ")
                self.atm.withdraw(amount)
                print(f"success! withdraw ${amount}")
                break
            except ValueError as e:
                print(e)

    def run(self):
        while True:
            self.display_menu()

            choice = input("Please choose an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                history = self.atm.check_history()
                if not history:
                    print("No transactions yet.")
                else:
                    for h in history:
                        print(h)
            elif choice == "5":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. please try again.")

def main():
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()
