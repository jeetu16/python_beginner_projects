# Loop
#   Ask : roll the dice?
#   If user enters y
#       Generate two random number
#       Print them
#   If user enters n
#       terminate the game
#   Else 
#       Print invalid choice
# Print Thank you message 
import random;

while True:
    command = str(input("Roll the dice? (y/n): "))
    if command.lower() == 'y':
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print(f"({first}, {second})")
    elif command.lower() == 'n':
        break
    else:
        print("Invalid choice!")
        continue
print("Thanks for playing!")