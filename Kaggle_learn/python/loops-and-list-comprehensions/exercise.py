# loops_exercises.py
import random


def has_lucky_number(nums):
    """Return True if the list contains at least one number divisible by 7."""
    for num in nums:
        if num % 7 == 0:
            return True
    return False


def elementwise_greater_than(L, thresh):
    """Return a list of booleans where each value indicates if element > thresh."""
    return [ele > thresh for ele in L]


def menu_is_boring(meals):
    """Return True if the same meal is served two days in a row."""
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False


# --- Slot Machine Simulation ---
def play_slot_machine():
    """
    Simulates a slot machine.
    Most of the time returns 0.
    Occasionally returns a big reward.
    """
    outcomes = [0] * 95 + [5, 10, 50, 100, 500]
    return random.choice(outcomes)


def estimate_average_slot_payout(n_runs):
    """Run slot machine n_runs times and return average net profit per run."""
    payouts = [play_slot_machine() - 1 for _ in range(n_runs)]
    return sum(payouts) / n_runs


# --- Test Block ---
if __name__ == "__main__":

    print("Lucky number test:", has_lucky_number([1, 2, 14, 3]))
    print("Elementwise test:", elementwise_greater_than([1, 2, 3, 4], 2))
    print("Menu boring test:", menu_is_boring(["Pizza", "Burger", "Burger", "Salad"]))

    print("Estimated slot payout (100000 runs):",
            estimate_average_slot_payout(100000))