import random



Guess = int(input("Guess a number between 1 and 6: "))
number = random.randint(1,6)
attempts = 1

while True:
    if Guess == number:
        print("You guessed the correct number!")
        if attempts == 1:
            print("Perfect! You guessed it on the first try!")
        print(f"Number of attempts: {attempts}")
        break
    else:
        Guess = int(input("Guess a number between 1 and 6: "))
        attempts += 1
# shuffle: shuffles the elements of a list in place, meaning it randomly rearranges the order of the elements in the list. It does not return a new list; instead, it modifies the original list directly.

Cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
random.shuffle(Cards)
print("Shuffled cards:", Cards)