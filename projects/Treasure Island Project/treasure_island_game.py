print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

action = input("There are two ways , Go either left or right \nType left or right ")

if action == "left":
    action=input("There is a lake \nEither swim or wait \nType swim or wait ")
    if action == "wait":
        action=input("There are 3 doors.\n Red, Blue and Green\n Select one door")
        if action == "yellow":
            print("You Win! ")
        elif action == "blue":
            print("Eaten by beasts.\nGame Over")
        elif action == "red":
            print("Burned by fire\nGame Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout\n Game Over.")
else:
    print("Fall into a hole \nGame Over.")


