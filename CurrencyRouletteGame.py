import requests
import random


def get_money_interval(difficulty):
    try:
        url = "https://api.freecurrencyapi.com/v1/latest?apikey=LaH76DonwIWCOTPUtMWECgG5KOv2P0E2rkiN6tQr&currencies=ILS"
        response = requests.request("GET", url)
        current_rate = response.json()['data']["ILS"]
        total_value = random.randint(1, 100)

        low_interval = total_value - (5 - difficulty) * current_rate
        high_interval = total_value + (5 - difficulty) * current_rate
        return {
            'low': low_interval,
            'high': high_interval
        }
    except Exception as ex:
        print("Failed to get Currency from the api")
        return None


def get_guess_from_user(lower, higher):
    while True:
        try:
            return float(input(f"Guess the secret value of, The number is between: {lower} and {higher}: "))
        except Exception as ex:
            print("Incorrect Format, Please enter a float number")


def play(difficulty):
    money_interval = get_money_interval(difficulty)
    if money_interval is None:
        return False
    low = money_interval['low']
    high = money_interval['high']
    user_guess = get_guess_from_user(low, high)
    if low <= user_guess <= high:
        print("Congrats!, You guesses correctly!")
        return True
    else:
        print("Oops!, You didn't guess the correct number, Please try again!")
        return False
