# 1. Initialize the inventory with some items
# We use a nested dictionary: keys are item names, values are dictionaries of details
inventory = {
    "Health Potion": {"price": 20, "stock": 5},
    "Mana Potion": {"price": 15, "stock": 8},
    "Iron Sword": {"price": 150, "stock": 2},
}

def display_inventory():
    """Prints the current inventory in a nice format."""
    print("\n--- Current Shop Inventory ---")
    for item, details in inventory.items():
        print(f"Item: {item} | Price: {details['price']} gold | Stock: {details['stock']}")
    print("------------------------------\n")

# --- Let's test some Dictionary Operations ---

# Display starting inventory
display_inventory()

# 2. UPDATE: Someone bought a Health Potion, decrease the stock
print("--- Action: A hero buys a Health Potion! ---")
inventory["Health Potion"]["stock"] -= 1
display_inventory()

# 3. ADD: Restock and add a brand new item to the dictionary
print("--- Action: Restocking and adding a 'Fire Scroll' ---")
inventory["Fire Scroll"] = {"price": 50, "stock": 4}
display_inventory()

# 4. READ/CHECK: Check if an item exists before trying to look it up
search_item = "Stealth Cape"
print(f"--- Action: Checking if we sell '{search_item}' ---")
if search_item in inventory:
    print(f"Yes! We have {inventory[search_item]['stock']} in stock.")
else:
    print(f"Sorry, we don't carry '{search_item}' in this shop.")
print()

# 5. DELETE: A thief stole all the Iron Swords! Remove it from the dictionary
print("--- Action: Iron Swords were discontinued/stolen! ---")
del inventory["Iron Sword"]
display_inventory()

