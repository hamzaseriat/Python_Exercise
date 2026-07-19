while True:
    age_input = input("Enter your age: ").strip()
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number for age.")

print(f"You are {age} years old.")

# exercise 2
food = input("Enter a food you like (q to quit): ").strip()
while food.lower() != "q":
    if food:
        print(f"You like {food}.")
    else:
        print("Please enter a food or q to quit.")
    food = input("Enter another food you like (q to quit): ").strip()
print("Bye!")