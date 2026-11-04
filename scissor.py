import random

CHOICES = ("r", "p", "s")
NAMES = {"r": "rock", "p": "paper", "s": "scissor"}
WINS = {"r":"s", "p":"r", "s":"p"}

options = ("r", "p", "s")

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