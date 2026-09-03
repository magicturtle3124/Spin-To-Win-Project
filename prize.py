import random

prizes = [
    "the worst outcome",
    "100 dollars",
    "50 dollas",
    "1000 dollars",
    "honey mamas",
    "bobo bar",
    "Rivian",
    "A house in Boulder",
    "An Alaskan Bullworm",
    "An Alaskan Cruise"
]

def get_random_prize():
    return random.choice(prizes)