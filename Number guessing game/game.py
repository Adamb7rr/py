from random import randint

def current_number(x, y):
    return randint(x, y)

def guess():
    while True:
        try:
            guess = int(input("Guess a number: "))
            break
        except ValueError:
            print("U should write only numbers")
    return guess

def get_bounds():
    while True:
        try:
            lower = int(input("Enter Lower bound: "))
            upper = int(input("Enter Upper bound: "))
            if lower >= upper:
                print("Lower bound must be less than upper bound.")
                continue
            return lower, upper
        except ValueError:
            print("Please enter valid numbers.")

def game():
    lower, upper = get_bounds()

    print("\tYou've only 7 chances to guess the integer!")

    tries = 7
    n = 1
    number = current_number(lower, upper)

    while True:
        user_guess = guess()
        if user_guess == number and tries > 0:
            print(f"Congratulations you did it in {n - 1} try.")
            break
        elif user_guess < number and tries > 0:
            print(f"Guess {n}: {user_guess} -> Too Low, (you have {tries - 1})")
            tries -= 1
            n += 1
        elif user_guess > number and tries > 0:
            print(f"Guess {n}: {user_guess} -> Too High, (you have {tries - 1})")
            tries -= 1
            n += 1
        else:
            print("You Lost, you have no tries.")
            break
    print(f"Total Guessess: {n - 1}")

game()
