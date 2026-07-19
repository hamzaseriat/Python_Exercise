import math

def calculate_hypotenuse(a,b):
    first = a ** 2;
    second = b ** 2;
    return math.sqrt(first + second);


# math.sqrt fuction is used to calculate the square root of the sum of the squares of the two sides.
side1 = float(input("Enter the length of the first side: "));
side2 = float(input("Enter the length of the second side: "));
hypo = calculate_hypotenuse(side1, side2);
print(f"The length of the hypotenuse is: {hypo}");

