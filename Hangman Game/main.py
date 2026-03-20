import random
from hangman_words import word_list

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

placeholder = ""
display = ""
game_over = False
guessed_letters = []
lives = 6

for letter in chosen_word:
    placeholder += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()
    if (guess not in chosen_word) and (guess not in guessed_letters):
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose! \n{chosen_word}")
    guessed_letters.append(guess) # guess must only be added to list after we checked if its already in the list and prevent life loss from guessing wrong letter twice
    for guess in guessed_letters:
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
    print(display)
    print("Number of lives: ", lives)
    if "_" not in display:
        game_over = True
        print(f"You win!")

    print(stages[lives])
