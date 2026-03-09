import random

words = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

def get_random_word(words):
    """Selects a random word from a list"""
    return random.choice(words)


def play_game():
    """Guess each letter of the secret word. For every wrong
    guess, the snowman melts"""

    secret_word = get_random_word(words)
    print("Welcome to the Snowman Meltdown Game!")
    print(f"Secret word selected is: {secret_word}")

    for i in range(len(secret_word)):
        mistakes = 0
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            continue
        else:
            mistakes += 1
            print(f"You made wrong guess")
            continue

    print(f"The secret word is : {secret_word}")




if __name__ == "__main__":
    play_game()