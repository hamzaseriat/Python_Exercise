print("Welcome! Do you wanna buy this house [Y/N]?");
for_sale = (input("Enter your response: ")).upper();


if for_sale == "Y":
    print("This item is for sale. ")
elif for_sale == "N":
    print("You cannot buy this " "item.")
else:
    print("Invalid response. Please enter Y or N.")
Online = True
if Online:
    print("Available for online purchase.")
else:
    print("Not available for online purchase.")