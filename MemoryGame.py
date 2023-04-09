import os
import random
from time import sleep

import Helpers

display_time = 0.7


def generate_sequence(difficulty):
    random_numbers = []
    for i in range(difficulty):
        random_numbers.append(random.randint(1, 101))
    print(f"The numbers will be shown for {display_time} seconds")
    print(random_numbers)
    sleep(display_time)
    Helpers.clear_console()

    return random_numbers


def get_list_from_user(difficulty):
    print(f"Enter your guesses, a Quick help, there were {difficulty} numbers in the list")
    user_guesses = []
    for i in range(difficulty):
        user_guesses.append(int(input(f"Enter Number # {i + 1} ")))
    return user_guesses


def is_list_equal(random_numbers, user_guesses):
    if random_numbers == user_guesses:
        print("Congrats!, The two lists are equal!")
        return True
    else:
        print("Oops!, You didn't get it this time!, Try again!!")
        return False


def play(difficulty):
    random_numbers = generate_sequence(difficulty)
    user_guesses = get_list_from_user(difficulty)
    return is_list_equal(random_numbers, user_guesses)
