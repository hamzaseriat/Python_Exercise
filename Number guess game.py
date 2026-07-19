import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
is_running = True


print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}. Can you guess what it is?")

 while is_running:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < lowest_num or guess > highest_num:
        print(f"Please guess a number between {lowest_num} and {highest_num}.")
        continue

    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} correctly!")
        is_running = False