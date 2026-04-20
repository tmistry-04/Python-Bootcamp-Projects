import random

from game_data import data

def extract_data(account):
    name = account['name']
    monthly_listeners = account['monthly_listeners']
    description = account['description']
    country = account['country']
    print(f"{name}, a {description}, from {country}")
    return monthly_listeners

accountA = random.choice(data)
accountB = random.choice(data)
current_score = 0

while True:
    print("Compare A: ")
    A = extract_data(accountA)
    print("\nAgainst B: ")
    B = extract_data(accountB)

    if A>B:
        winner = "A"
        winning_acc = accountA
    else:
        winner = "B"
        winning_acc = accountB

    guess = input("\nWho has more monthly listeners on Spotify? A or B: ")
    if guess == winner:
        current_score += 1
        print("\n" * 20, f"You're right! Current score: {current_score}")
        accountA = winning_acc
        accountB = random.choice(data)
        # if A and B are the same account, choose a new B
        if accountA == accountB:
            accountB = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break
