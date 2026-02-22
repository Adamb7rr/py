class Calculator:
    def __init__(self):
        self.history = []

    def calc(self, num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        else:
            raise ValueError("Invalid operator")

    def add_history(self, expression):
        self.history.append(expression)

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            for item in self.history:
                print(item)

    def get_number(self, prompt):
        while True:
            try:
                return float(input(f"Enter {prompt}: "))
            except ValueError:
                print("Invalid number.")

    def get_operator(self):
        allowed = ('+', '-', '*', '/', '%', '**')
        while True:
            operator = input("Enter operator (+ - * / % **): ")
            if operator in allowed:
                return operator
            print("Invalid operator.")

def main():
    calc = Calculator()

    while True:
        num1 = calc.get_number("Num1")
        operator = calc.get_operator()
        num2 = calc.get_number("Num2")

        try:
            result = calc.calc(num1, operator, num2)
            expression = f"{num1} {operator} {num2} = {result}"
            calc.add_history(expression)
            print(expression)
        except ValueError as e:
            print(e)

        choice = input("\n(y) again | (h) history | (n) exit: ").lower()

        if choice == 'h':
            calc.show_history()
        elif choice == 'n':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()