operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = None
if operator == '+':
    result = round(num1 + num2, 2)
elif operator == '-':
    result =round(num1 - num2, 2)
elif operator == '*':
    result = round(num1 * num2, 2)
elif operator == '/':
    if num2 != 0:
        result = round(num1 / num2, 2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")

if result is not None:
    print(f"The result is: {result}")
