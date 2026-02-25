# 1. sign function
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# 2. to_smash function with correct grammar
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after
    distributing the given number of candies evenly between 3 friends.
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3


# 3. prepared_for_weather (original buggy version)
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday


# Example failing test case
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

print("Prepared for weather:", prepared_for_weather(
    have_umbrella, rain_level, have_hood, is_workday
))


# 4. concise_is_negative
def is_negative(number):
    if number < 0:
        return True
    else:
        return False


def concise_is_negative(number):
    return number < 0


# 5a. Hotdog topping functions
def onionless(ketchup, mustard, onion):
    return not onion


def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion


# 5b. Plain hotdog
def wants_plain_hotdog(ketchup, mustard, onion):
    return not (ketchup or mustard or onion)


# 5c. Exactly one sauce (ketchup or mustard but not both)
def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)


# 6. Exactly one topping (using boolean to integer conversion)
def exactly_one_topping(ketchup, mustard, onion):
    return (ketchup + mustard + onion) == 1


# 7. Basic blackjack strategy example
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """
    Simple strategy:
    - Hit if player total is less than 17
    - Otherwise stay
    """
    return player_total < 17


# Example manual tests
if __name__ == "__main__":
    print("sign(-5):", sign(-5))
    print("sign(0):", sign(0))
    print("sign(10):", sign(10))

    print("to_smash(91):", to_smash(91))
    print("to_smash(1):", to_smash(1))

    print("is_negative(-3):", is_negative(-3))
    print("concise_is_negative(5):", concise_is_negative(5))

    print("wants_plain_hotdog(False, False, False):",
          wants_plain_hotdog(False, False, False))

    print("exactly_one_topping(True, False, False):",
          exactly_one_topping(True, False, False))