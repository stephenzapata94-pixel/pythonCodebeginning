import random

CHOICES = ("r", "p", "s")
NAMES = {"r": "rock", "p": "paper", "s": "scissor"}
WINS = {"r":"s", "p":"r", "s":"p"}

options = ("r", "p", "s")

wins = 0
loses = 0
draws = 0

while True:
# prompts players to choose a weapon until it matches one of the choices
    player = input("Please choose your weapon:")
    while player not in CHOICES:
        print(f"{player} is not a weapon")
        player = input("Please choose your weapon:")
    print(f"Your weapon of choice is {player}!")

# the computer will only choice between the options section above
    computer = random.choice(options)
    print(f"Computer chose the weapon {computer}!")

    if player == computer:
        print("It's a DRAW")
    elif WINS[player] == computer:
        print("Player wins")
    else:
        print("Computer wins")

    if WINS[player] == computer:
        wins += 1
    elif player == computer:
        draws += 1
    else:
        loses += 1
    print(f"Wins: {wins}, Loses: {loses}, Draws: {draws}")


# this will ask players if they want to play again or not and give a farewell
    try_again = input("Do you want to play again? (y/n): ") .strip() .lower()
    if try_again != "y":
        print("Come back again another time!")
        break
    
        