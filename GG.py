import random
random_number = random.randint(1,10)



while True:
    user_guess = int(input("Pick a number from 1 to 10: " ))
    if user_guess > 10:
        print("Number outside range")
    elif user_guess < 1:
            print("Number outside range")
    if user_guess > random_number:
        print("Guess Lower")
    elif user_guess < random_number:
        print("Guess Higher")
    else:
        print(f"Your guess of {random_number} was correct")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)    
            user_guess = None
        else:
            print("Thank you for playing!") 
            break
