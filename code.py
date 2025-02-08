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