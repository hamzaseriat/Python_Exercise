import math


def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle is: {area}")

def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2*math.pi * radius;

circumference = calculate_circumference(radius);
print(f"the circumference of the circle is. {circumference}");