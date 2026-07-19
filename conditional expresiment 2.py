age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)
# This part comlately different from the previous snippet, as it uses a conditional expression (ternary operator) to determine if the user is an adult or a minor based on their age input. The previous snippet focused on logical operations and conditions related to weather and temperature, while this snippet is a simple age check.

admin_status = "Admin"

access_level = "Full Access" if admin_status == "Admin" else "Limited Access"
print(access_level)