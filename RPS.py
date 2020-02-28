import random
print("Rock....")
print("Paper....")
print("Scissors....")

while True:
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2 :
        player = input ("Player, make your move: ").lower()
        rand_num = random.randint(0,2)
        if rand_num == 0:
            computer = "rock"
        elif rand_num == 1:
            computer = "paper"
        else:
            computer = "scissors"
        print(f"Computer plays {computer}")    

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Player  wins!")
                player_wins +=1
            elif computer == "paper":
                print("Computer wins!")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player wins!")
                player_wins +=1
            elif computer == "scissors":
                print("Computer wins!")
                computer_wins += 1
        elif player == "scissors":
            if computer == "paper":
                print("Player wins!")
                player_wins +=1
            elif computer == "rock":
                print("Computer wins!")
                computer_wins += 1
        else:
            print("something went wrong")
            print("please enter a valid move")
    print(f"FINAL SCORE.... \n Player: {player_wins} \n Computer: {computer_wins}")
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "y":
        pass
    else:
        print("Thank you for playing!") 
        break
