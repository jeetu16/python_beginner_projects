import random

while True:
    try:
        print("Enter the minimum and maximum range for guessing!")
        min = int(input("Minimum Range: "))
        max = int(input("Maximum Range: "))
        if min > max:
            print(f"Try again!. Minimum range should be less than to Maximum range")
            continue
        number_to_guess = random.randint(min, max)
        count = 0
        limit = 5

        while True:
            count += 1
            try:
                if limit == 0:
                    print(f"You tried maximum number of times(5). Number was the {number_to_guess}!")
                    break
                print(f"You have {limit} chance!\n")
                guess = int(input(f"Guess the number (between {min} and {max}): "))
                if guess < number_to_guess:
                    print("Too low! Try again")
                elif guess > number_to_guess:
                    print("Too high! Try again")
                else:
                    print(f"Congratuations! You guessed the number {number_to_guess} in {count} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number")
                continue
            limit -= 1
        break
    except ValueError:
        print("Please enter valid range")