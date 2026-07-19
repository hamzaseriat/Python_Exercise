menu = {"Pizza": 10, "Nachos": 5, "Burger": 8, "Salad": 6,"Hot Dog": 5.44, "Fries Chicken": 6.99}
cart = []
total = 0;

print("----Menu----")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------")

while True: 
    food = input("Enter the food item you want to order (or type 'done' to finish): ")
    if food.lower() == "done":
        break
    elif menu.get(food) is not None:
        cart.append(food)
       

for food in cart:
    total += menu[food]

print("Your order:")
for food in cart:
    print(f"{food:}: ${menu[food]:.2f}")
print(f"Total: ${total:.2f}")