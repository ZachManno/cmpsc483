import random

introductions = [
    "There is",
    "There are",
    "There exists",
    "We have",
    "Once upon a time, there were",
    "In this problem, we have"
]

def generate_intro():
    return random.choice(introductions) + " "
