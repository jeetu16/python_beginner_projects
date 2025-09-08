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