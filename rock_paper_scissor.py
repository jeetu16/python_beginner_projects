
import random;

rps = {
    'r' : "🪨" ,
    'p': "📄",
    's': "✂️"
}
choices = ['r', 'p', 's']

# Get the User Choice
def getUserChoice():
    while True:
        userChoice = input("Rock, paper, or scissors? (r,p,s): ").lower()
        if userChoice in choices:
            return userChoice
        else:
            print("Invalid choice! Try Again.")

# Display the choices
def displayChoices(userChoice, computerChoice):
    print(f"You chose {rps[userChoice]}")
    print(f"Computer chose {rps[computerChoice]}")


# Determine the winner
def determineWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        print("It's Tie")
    elif (
        (userChoice == 'p' and computerChoice == 'r') or 
        (userChoice == 'r' and computerChoice == 's') or 
        (userChoice == 's' and computerChoice == 'p')
    ):
        print("You Win!")
    else:
        print("You Lose!")

# Want to continue the game
def shouldContinueGame():
    isContinue = False
    while True:
        shouldContinue = input("Continue? (y/n): ").lower()
        if shouldContinue != 'y' and shouldContinue != 'n':
            print("Invalid choice! Try Again.")
            continue
        elif shouldContinue == 'y':
            isContinue = True
        else:
            isContinue = False
        return isContinue

# Play the game
def playGame():
    while True:
        userChoice = getUserChoice()
        computerChoice = random.choice(['r','p','s'])
        
        displayChoices(userChoice, computerChoice)

        determineWinner(userChoice, computerChoice)

        shouldContinue = shouldContinueGame()

        if shouldContinue:
            continue
        else:
            break

playGame()
print("Thanks for playing!")


