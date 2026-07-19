unit = input("Is that celcius or fahrenheit? (C/F): ").strip().lower()
if unit == 'c':
    temp = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {fahrenheit}°F")
elif unit == 'f':
    temp = float(input("Enter the temperature in Fahrenheit: "))
    celcius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celcius}°C")
else:
    print("Invalid input. Please enter 'C' for Celcisus or 'F' for Fahrenheit.")

    