# validate user input
# username is no more than 20 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter a username: ")

if username.__len__() > 20:
    print("Username must be no more than 20 characters.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")  
elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")

else:
    print("Username is valid.")
