# lists_exercises.py

def select_second(L):
    """Return the second element of the given list.
    If the list has no second element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]


def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names,
    return the 2nd player (captain) from the last listed team.
    """
    return teams[-1][1]


def purple_shell(racers):
    """Swap first and last racer in-place."""
    racers[0], racers[-1] = racers[-1], racers[0]


def fashionably_late(arrivals, name):
    """Return whether the guest arrived fashionably late."""
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


# Optional: Add a test block so it runs when executed directly
if __name__ == "__main__":
    print(select_second([1, 2, 3]))  # 2

    teams = [
        ["Coach1", "Captain1", "Player1"],
        ["Coach2", "Captain2", "Player2"]
    ]
    print(losing_team_captain(teams))  # Captain2

    racers = ["Mario", "Bowser", "Luigi"]
    purple_shell(racers)
    print(racers)  # ['Luigi', 'Bowser', 'Mario']

    party = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
    print(fashionably_late(party, "Mona"))  # True