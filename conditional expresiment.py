num = int(input("Enter a number: "))
print("The number is positive.") if num > 0 else print("The number is not positive.")

result = "EVEN" if num % 2 == 0 else "ODD"
print(f"Your number is {result}.")

firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
max_num = firstnum if firstnum > secondnum else secondnum
print(f"The maximum number is {max_num}.")

min_num = firstnum if firstnum < secondnum else secondnum
print(f"The minimum number is {min_num}.")

if firstnum == secondnum:
    print("Both numbers are equal.")

average = float(firstnum + secondnum) / 2
print(f"The average of the two numbers is {average}.")

