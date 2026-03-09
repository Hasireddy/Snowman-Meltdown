import random

words = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word(words):
    return random.choice(words)


print(get_random_word(words))