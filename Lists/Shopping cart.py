import time

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item (q to quit):")
    if food == "q":
        break
    price = float(input(f"Enter the price of {food}: "))
    foods.append(food)
    prices.append(price)
    total += price

print("You have entered the following food items and their prices:")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
print(f"Total: ${total:.2f}")

for food in foods:
    print(f"Preparing {food}...")
    time.sleep(1)
    print(f"{food} is ready!")