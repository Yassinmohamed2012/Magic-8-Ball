import random

responses = ["yes definetily",'no, not now','ask again later ','its certain','very doubtful','outlook is good','better not tell you now','concentrate and ask again']

def get_random_response():
    return random.choice(responses)