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