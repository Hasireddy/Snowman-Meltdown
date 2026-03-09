import random
from ascii_art import STAGES

words = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word(words):
    """Selects a random word from a list"""
    return random.choice(words)


def play_game():
    """Guess each letter of the secret word. For every wrong
    guess, the snowman melts"""

    secret_word = get_random_word(words).strip()
    print("Welcome to the Snowman Meltdown Game!")
    print(STAGES[0])

    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES)-1

    while(mistakes < max_mistakes):
        display_game_state(secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        while len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        if guess not in secret_word:
            mistakes += 1
            print(f"You made {mistakes} wrong guess")
            print(STAGES[mistakes])
        else:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
            print("Correct guess!")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(secret_word, guessed_letters)
            print("Saved the Snowman!")
            print(f"The secret word is : {secret_word}")
            return

    print(f"Snow man melted. The secret word is : {secret_word}")


def display_game_state(secret_word, guessed_letters):
    """Displays the current stage and the secret word
    with underscores for unguessed letters"""

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(f"word: {display_word}")
