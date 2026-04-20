import random

NUMBER = random.randint(1, 100)

difficulty = input("Welcome to Number Guessing Game!\n "
      "I'm thinking of a number between 1 and 100.\n"
      "Choose a difficulty level: Type 'easy' or 'hard': ")

def game(attempts):
    total_attempts = attempts
    while True:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess == NUMBER:
            print(f"You win! The number was {NUMBER}. You got it in {total_attempts-attempts} attempts!")
            break
        elif guess < NUMBER:
            print(f"Too low, try again.\nYou have {attempts} attempts left")
        elif guess > NUMBER:
            print(f"Too high, try again.\nYou have {attempts} attempts left")

        if attempts == 0:
            print(f"You lost! The number was {NUMBER}")
            break


if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)

