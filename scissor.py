Rock = "r"
Paper = "p"
Scissor = "s"  

player = input("Enter your choice:")
print("Player choice is:", player)
computer = input("Enter computer choice:")
print("Computer choice is:", computer)

if player == computer:
    print("It's a DRAW")
elif player == Rock and computer == Scissor or player == Scissor and computer == Paper or player == Paper and computer == Rock:
    print("Player wins")
else:
    print("Computer wins")