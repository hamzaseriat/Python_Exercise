fruits = ["apple", "banana", "cherry", "date", "elderberry"]
grociers = ["milk", "bread", "eggs", "cheese", "butter"]
male_names = ["John", "Michael", "David", "James", "Robert"]

collections = [fruits, grociers, male_names]

for food in collections:
    for item in food:
        print(item,end=' ')
    print("\n")


# now we will print a 2D list of numbers in a num_pad format
num_pad = [(1, 2, 3), (4, 5, 6), (7, 8, 9), ("*",0,"#")]
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print("\n")