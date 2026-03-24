import random
print("Welcome to the Rock Paper Scissor Game")
print("What do you choose")

move = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_move= random.randint(0,2)
if move == 0 :
    if computer_move == 0 :
        print("Computer choose Rock")
        print("Its a Tie")

    elif computer_move == 1 :
        print("Computer choose Paper")
        print("Computer Win!")

    else:
        print("Computer choose Scissor")
        print("You Win!")

elif move == 1 :
    if computer_move == 0:
        print("Computer choose Rock")
        print("You Win!")

    elif computer_move == 1:
        print("Computer choose Paper")
        print("Its a Tie")

    else:
        print("Computer choose Scissor")
        print("Computer Win!")

elif move == 2 :
    if computer_move == 0:
        print("Computer choose Rock")
        print("Computer Win!")

    elif computer_move == 1:
        print("Computer choose Paper")
        print("You Win!")

    else:
        print("Computer choose Scissor")
        print("Its a Tie")