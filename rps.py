import sys
import random
from enum import Enum

def RPS():
    game_count=0
    player_wins=0
    python_wins=0

    

    def play_RPS():
        nonlocal player_wins
        nonlocal python_wins
        
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
        

        def decide_winner(player , computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3 :
                player_wins += 1
                return "you win!🏆"
            elif player == 2 and computer == 1 :
                player_wins += 1
                return "you win!🏆"
            elif player == 3 and computer == 2 :
                player_wins += 1
                return "you win!🏆"
            elif player == computer :
                return "Tie Game!"
            else :
                python_wins += 1
                return "🐍  Python win!"
        
        game_result = decide_winner(player , computer)
        
        print(game_result)
        
        
        nonlocal game_count
        game_count += 1
        
        print("\nGame Count " + str(game_count))
        print("\nplayer wins " + str(player_wins))
        print("\npython wins " + str(python_wins))
        
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
            
            
    return play_RPS

play = RPS()


play()
            


