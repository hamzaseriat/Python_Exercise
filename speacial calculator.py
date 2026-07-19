# python compound calculator

principal = 0.0
rate = 0.0
years = 0

while principal <= 0:
    try:
        principal = float(input("Enter principal: "))
        if principal <= 0:
            print("Principal must be greater than zero.")
    except ValueError:
        print("Please enter a valid number for principal.")

while rate <= 0:
    try:
        rate = float(input("Enter annual interest rate (%): "))
        if rate <= 0:
            print("Rate must be greater than zero.")
    except ValueError:
        print("Please enter a valid number for rate.")

while years <= 0:
    try:
        years = int(input("Enter time in years: "))
        if years <= 0:
            print("Time must be greater than zero.")
    except ValueError:
        print("Please enter a valid whole number for years.")

amount = principal * (1 + rate / 100) ** years
print(f"Balance after {years} year(s): ${amount:.2f}")
