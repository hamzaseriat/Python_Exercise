import time


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number >= 1:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(1, number + 1):
        print(i)
        if i < number:
            time.sleep(1)


if __name__ == "__main__":
    main()