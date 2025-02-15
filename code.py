def get_user_guess():
    while True:
        try:
            guess=int(input("enter your guess(1-100)"))
            if i <= guess <= 100:
                return guess
            else:
                print("please enter a valid no. between 1-100")
        except ValueError:
            print("invalid input, please enter a valid no.")
import random

responses = ["yes definetily",'no, not now','ask again later ','its certain','very doubtful','outlook is good','better not tell you now','concentrate and ask again']

def get_random_response():
    return random.choice(responses)
<<<<<<< HEAD
def play_again():
    while True:
        choice=input("do you want to ask another question(yes/no):  ").strip().lower()
        if choice=="yes":
            return True
        elif choice=="no":
            print("thanks for playing, goodbye")
            return False
        else:
            print("invalid input, please enter yes or no")
         
def display_response(response):
    print("\n🔮 The Magic 8-Ball says:", response )
=======
>>>>>>> parent of b4bad0e (Merge branch 'feature-playe-again')
