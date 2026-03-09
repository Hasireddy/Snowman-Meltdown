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

    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")



if __name__ == "__main__":
    play_game()