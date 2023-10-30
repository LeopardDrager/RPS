import random

def userChoice():
    rpsUser = input("Pick rock, paper, or scissors! ")
    return rpsUser

def computerChoice():
    listOfOptions = ["rock", "paper", "scissors"]
    return random.choice(listOfOptions)

def result(computer, player):
    if computer == player:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def game():
    rpsUser = userChoice().lower()
    compChoice = computerChoice()
    print(f"You chose {rpsUser}! The computer chose {compChoice}!")
    outcome = result(compChoice, rpsUser)
    print(outcome)

# Call the game function to play game()
game()
    
    

    
