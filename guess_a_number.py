import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number ( 1- 100):")
    #print("If you want to quit press : q")
    #if player_input == "q":
    #    print("You have decided to quit!")
    #    break
    if not player_input.isdigit():
        print("Invalid input!")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low!")
