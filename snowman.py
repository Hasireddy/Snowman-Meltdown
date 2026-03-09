
from game_logic import get_random_word, play_game, display_game_state


if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nPlay again? (y/n): ").lower()

        if replay == "y":
            play_game()
            break
