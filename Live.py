from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_currency_roulette
from Score import add_score
import Helpers


def welcome(name):
    return f"Hello {name} and welcome to the World Of Games(WoG)." \
           f"Here you can find many cool games to play."


def load_game():
    choice = 4
    difficulty = 6
    while 1 > choice or choice > 3:
        try:
            choice = int(input("Please choose a game to play:\n"
                               "1. Memory Game\n"
                               "2. Guess Game\n"
                               "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
        except Exception as ex:
            print("Incorrect Input")

    while 1 > difficulty or difficulty > 5:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
        except Exception as ex:
            print("Incorrect Input")

    # Helpers.clear_console()
    is_user_won = False
    if choice == 1:
        print("Starting Memory Game!")
        is_user_won = play_memory_game(difficulty)
    elif choice == 2:
        print("Starting Guess Game!")
        is_user_won = play_guess_game(difficulty)
    else:
        print("Starting Currency Roulette!")
        is_user_won = play_currency_roulette(difficulty)

    if is_user_won:
        add_score(difficulty)
