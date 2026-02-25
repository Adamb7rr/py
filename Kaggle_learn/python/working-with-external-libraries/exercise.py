# advanced_exercises.py

import random
import matplotlib.pyplot as plt


# -------------------------------------------------
# 1️⃣  Graph Prettifier
# -------------------------------------------------

def prettify_graph(graph):
    """
    Modify the given graph:
    - Add title
    - Make y-axis start at 0
    - Label y-axis as 'Balance'
    - Format y-axis ticks as dollar amounts
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")

    # Bonus: format y-axis as dollar amounts
    ticks = graph.get_yticks()
    new_labels = ['${}'.format(int(t)) for t in ticks]
    graph.set_yticklabels(new_labels)


# Example demo graph (since we don’t have jimmy_slots module)
def demo_graph():
    balance = [200]
    for _ in range(500):
        balance.append(balance[-1] + random.choice([-1, -1, -1, 5]))

    fig, ax = plt.subplots()
    ax.plot(balance)
    prettify_graph(ax)
    plt.show()


# -------------------------------------------------
# 2️⃣  Luigi’s Best Items (Fixed Version)
# -------------------------------------------------

def best_items(racers):
    """
    Return a dictionary mapping items to how many times
    they were picked up by first-place finishers.
    """
    winner_item_counts = {}

    for index in range(len(racers)):
        racer = racers[index]

        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer['name'] is None:
            print(
                f"WARNING: Encountered racer with unknown name on iteration "
                f"{index+1}/{len(racers)}"
            )

    return winner_item_counts


# -------------------------------------------------
# 3️⃣  Blackjack Comparison
# -------------------------------------------------

def hand_total(hand):
    """Calculate blackjack total."""
    total = 0
    aces = 0

    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)

    total += aces

    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1

    return total


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2 in blackjack.
    """
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)

    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)


# -------------------------------------------------
# Test Block
# -------------------------------------------------

if __name__ == "__main__":

    # Demo 1: Graph
    demo_graph()

    # Demo 2: Best items
    sample = [
        {'name': 'Peach', 'items': ['green shell', 'banana'], 'finish': 3},
        {'name': 'Bowser', 'items': ['green shell'], 'finish': 1},
        {'name': None, 'items': ['mushroom'], 'finish': 2},
        {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
    ]

    print("Best items:", best_items(sample))

    # Demo 3: Blackjack
    hand1 = ['K', 'A']
    hand2 = ['7', '10', 'A']
    print("Hand1 beats Hand2?", blackjack_hand_greater_than(hand1, hand2))