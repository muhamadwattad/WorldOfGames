import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user():
    while True:
        try:
            return int(input("guess the number: "))
        except Exception as ex:
            print("Incorrect Format, Please enter an integer")


def compare_results(user_guess, random_number):
    if user_guess == random_number:
        print("Congrats! You found the number!")
        return True
    else:
        print("You didn't find the number, Try again!")
        return False


def play(difficulty):
    random_number = generate_number(difficulty)
    user_guess = get_guess_from_user()
    return compare_results(user_guess, random_number)
