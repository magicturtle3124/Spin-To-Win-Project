import random

prizes = [
    "the worst outcome",
    "100 dollars",
    "50 dollas",
    "1000 dollars",
    "honey mamas",
    "bobo bar",
    "Rivian",
    "A house in Boulder"
]

def get_random_prize():
    return random.choice(prizes)