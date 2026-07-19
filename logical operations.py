
def main():
    condition = input("Is it sunny? (yes/no): ")
    sunny = condition.strip().lower() == 'yes'

    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Please enter a valid number for the temperature.")
        return

    is_bad_temp = temp <= 0 or temp >= 100
    is_good_temp = 0 < temp < 100

    if is_bad_temp and not sunny:
        print("The temperature is bad and it is not sunny.")
    elif is_bad_temp and sunny:
        print("The temperature is bad but it is sunny.")
    elif is_good_temp and not sunny:
        print("The temperature is good but it is not sunny.")
    else:
        print("The temperature is good and it is sunny.")


if __name__ == '__main__':
    main()

