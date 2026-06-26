name = input("Enter your name: ")
length = len(name)
print("The length of your name is:", length)

# We will learn find method in this snippet. The find() method is used to search for a specific substring within a string and returns the index of the first occurrence of that substring. If the substring is not found, it returns -1. In this case, we are searching for the letter 'm' in the user's name and printing its index if found, or a message indicating that it was not found
# So if we use find() our purpose is to locate the posiiton of a specific charecter inside the function.
char = input("Enter a character to find in your name: ")
index = name.find(char)
if index != -1:
    print(f"The character '{char}' is found at index:", index)
# Now we talk about the capitalize() method. The capitalize() method is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. In this case, we are capitalizing the user's name and printing the result.

name_capitalized = name.capitalize()
print("Your name capitalized is:", name.capitalize())