import random
choices = ["rock", "paper", "scissors"]
running = True

while running:
    computer = random.choice(choices)
    player = input("rock, paper, or scissors: ")
    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    if player == "I quit":
        running == False

print("Thanks for playing")