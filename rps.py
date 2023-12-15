import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain : 
   
    playerChoice = input("\nEnter\n1 For Rock,\n2 For Paper,\n3 For Scisors:\n\n")

    player = int(playerChoice)

    if player < 1 | player > 3:
        sys.exit("You must enter 1,2 or 3")

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
    
    play = input("\nPlay again? \nY for Yes\nQ for Quit\n\n")
    
    
    if play.lower() == "y":
        continue
    else:
        print("🎂 🎂 🎂 🎂")
        print("Thank You for Playing!\n")
        playagain = False
sys.exit("Bye! 👋")
