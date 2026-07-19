# collection = single "variable" used to store multiple values in a single variable. In Python, there are several types of collections, including lists, tuples, sets, and dictionaries. Each type has its own characteristics and use cases.
 # Lists = [] ordered and changeable collection of items. Lists are defined using square brackets [] and can contain elements of different data types. They allow duplicate values and support indexing and slicing.
 # Tuples = () ordered and unchangeable collection of items. Tuples are defined using parentheses () and can also contain elements of different data types. They allow duplicate values and support indexing and slicing, but their elements cannot be modified after creation.
 # Sets = {} unordered and unchangeable collection of unique items. Sets are defined using curly braces {} or the set() constructor. They do not allow duplicate values and do not support indexing or slicing. Sets are useful for performing mathematical operations like union, intersection, and difference.
 # Dictionaries = {} unordered and changeable collection of key-value pairs. Dictionaries are defined using curly    

fruits = ["apple", "banana", "coconut"]

print(fruits[::-1])  # Output: ['coconut', 'banana', 'apple']
for x in fruits:
    print(x)  # Output: apple, banana, coconut (each on a new line)
    # if we wanna a help we can use dir() function to get the list of all attributes and methods of the list object.
    
fruits.append("cherry")  # Adds an item to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'coconut', 'cherry']