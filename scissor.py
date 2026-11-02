Rock = "r"
Paper = "p"
Scissor = "s"  

player = input("Enter your choice:")
print("Player choice is:", player)
computer = input("Enter computer choice:")
print("Computer choice is:", computer)

if player == computer:
    print("It's a DRAW")
elif player == Rock and computer == Scissor:
    print("Player wins")
elif player == Paper and computer == Rock:
    print("Player wins")
elif player == Scissor and computer == Paper:
    print("Player wins")
else:
    print("Computer wins")