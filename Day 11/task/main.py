import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_conversion(card_hand):
    # Ace flexibility - 11 can become a 1 to prevent going over 21:
    while sum(card_hand) > 21 and (11 in card_hand):
        card_hand[card_hand.index(11)] = 1

def blackjack():
    # list of players cards:
    player_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]
    bust = False

    ace_conversion(player_cards)
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    while sum(comp_cards) < 17:
        comp_cards.append(random.choice(cards))
    ace_conversion(comp_cards)

    if sum(comp_cards) > 21:
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
        print("Opponent went over. You win 😃")
        bust = True

    while not bust and input("Type 'y' to get another card, type 'n' to pass: ") == "y" and (sum(player_cards) <= 21):
        player_cards.append(random.choice(cards))
        ace_conversion(player_cards)

        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {comp_cards[0]}")


        if sum(player_cards) > 21: # if player busts, regardless of whether or not computer busts, player loses:
            print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
            print("You went over. You lose 😭")
            bust = True
            break

    # once user decides NOT to get another card, decide who wins so long as no one has been busted already:
    if not bust:
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
        if sum(player_cards) == sum(comp_cards) == 21 and len(comp_cards) == len(player_cards) == 2:
            print("You both had blackjacks! Draw!")
        elif (sum(player_cards) == 21) and len(player_cards) == 2:
            print("You win with a Blackjack 😎!")
        elif (sum(comp_cards) == 21) and len(comp_cards) == 2:
            print("You lose, opponent has Blackjack 😱")
        elif sum(player_cards) == sum(comp_cards):
            print("\nDraw")
        elif (sum(player_cards) <= 21) and (sum(player_cards) > sum(comp_cards)):
            print("\nYou win 😃")
        elif sum(player_cards) < sum(comp_cards) and sum(comp_cards) <= 21:
            print("\nYou lose 😭")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()

