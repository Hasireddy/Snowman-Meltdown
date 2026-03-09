import random

words = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word(words):
    """Selects a random word from a list"""
    return random.choice(words)


def play_game():
    """Guess each letter of the secret word. For every wrong
    guess, the snowman melts"""

    secret_word = get_random_word(words)
    print("Welcome to the Snowman Meltdown Game!")
    print(f"Secret word selected is: {secret_word}")

    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES)-1
    while(mistakes < max_mistakes):
        guess = input("Guess a letter: ").lower()
        if guess not in secret_word:
            mistakes += 1
            print(f"You made {mistakes} wrong guess")
            print(STAGES[mistakes])
            continue
        guessed_letters.append(guess)
    return mistakes, secret_word, guessed_letters


def display_game_state(secret_word, guessed_letters):
    """Displays the current stage and the secret word
    with underscores for unguessed letters"""

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + "_"
        else:
            display_word += "_"

        print(f"word: {display_word}")
        print("\n")