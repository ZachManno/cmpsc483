import random

### NOTE: look into online libraries that deal with plurals
### taxonomy for animals?

introductions = [
    "There is",
    "There are",
    "There exists",
    "We have",
    "Once upon a time, there were",
    "In this problem, there exists"
]

and_connectors = [
    "Also,",
    "Further,",
    "Furthermore,",
    "Don't forget that",
    "In addition",
    "To add,",
    "Plus,",
    "It's also worth mentioning that",
]

counting_solutions_intro = [
    "What is the amount of",
    "What is the count of",
    "Give the final count of",
    "Provide the final count of",
    "How many",
    "Count the number of"
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
    conclusion += objecttype.lower()
    #conclusion += " "
    if (bool(random.getrandbits(1))):
        conclusion += " "
        conclusion += random.choice(counting_solutions_conclusion)

    conclusion += "?"
    return conclusion