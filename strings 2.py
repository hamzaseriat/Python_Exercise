# upper function works on string and returns the string in uppercase letters. It does not work on integers or other data types.
words = input("Enter a string: ")
words = words.upper()
print(words)
# The lower() method is used to convert all characters in a string to lowercase. It does not work on integers or other data types.
words = input("Enter a string: ")
words = words.lower()
print(words)
# isdigit() method is used to check if all characters in a string are digits. It returns True if all characters are digits, and False otherwise. It does not work on integers or other data types.
words = input("Enter a string: ")
is_digits = words.isdigit()
print("All characters are digits: ", is_digits)
