import sys
import random
from enum import Enum

def play_RPS():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input("\nEnter\n1 For Rock,\n2 For Paper,\n3 For Scisors:\n\n")

    if playerChoice not in ["1","2","3"]:
        print("You must Enter 1 ,2 or 3")
        return play_RPS()
    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    
    print("\nYou Chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Computer Chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    


    if player == 1 and computer == 3 :
        print("you win!🏆")
    elif player == 2 and computer == 1 :
        print("you win!🏆")
    elif player == 3 and computer == 2 :
        print("you win!🏆")
    elif player == computer :
        print("Tie Game!")
    else :
        print("🐍  Python Win!")
    
    
    while True:
        playagain = input("\nPlay again? \nY for Yes\nQ for Quit\n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return play_RPS()
    else:
        print("🎂 🎂 🎂 🎂")
        print("Thank You for Playing!\n")
        sys.exit("Bye! 👋")
        
        
        
play_RPS()

