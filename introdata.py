import random

introductions = [
    "There is",
    "There are",
    "There exists",
    "We have",
    "Once upon a time, there were",
    "In this problem, we have"
]

and_connectors = [
    "Also,",
    "Further,",
    "Furthermore,",
    "Don't forget that",
    "In addition",
    "Plus,",
    "It's also worth mentioning that",
]

counting_solutions_intro = [
    "What is the total amount of",
    "What is the total count of",
    "Give the final total count of",
    "Provide the final total count of",
    "How many "
]

counting_solutions_conclusion = [
    "in the end",
    "in total",
    "in summary"
]

def generate_intro():
    return random.choice(introductions) + " "

def get_and_connector():
    return random.choice(and_connectors) + " "

def generate_conclusion(objecttype):
    conclusion = random.choice(counting_solutions_intro)
    conclusion += " "
    conclusion += objecttype

    if (bool(random.getrandbits(1))):
        conclusion += random.choice(counting_solutions_conclusion)

    conclusion += "?"
    return conclusion