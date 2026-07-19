# count() method is used to count the number of occurrences of a substring in a string. In this case, we are counting the number of hyphens ("-") in the phone number entered by the user.
phone_number = input("Enter your phone number: ")
result = phone_number.count("-")
print(result)

#   replace() method is used to replace all occurrences of a substring with another substring. In this case, we are replacing all hyphens ("-") in the phone number with an empty string, effectively removing them.
cleaned_phone_number = phone_number.replace("-", "")
print(cleaned_phone_number)

