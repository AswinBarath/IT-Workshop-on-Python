# d. Elaborate string operations such as string declaration, traversing, slicing, concatenating, and sorting
print("Program to demonstrate String Operations")

# String Declaration
animal = "Elephant"

# String Traversal
# Type 1:
for letter in animal:
    print(letter, end=" ")

# Type 2:
for letter in range(0, len(animal)):
    print(animal[letter])

# String Slicing
print(animal[0:3])
print(animal[3:])
print(animal[::2])

# String Concatenation
print('Track p' + animal[5:])

# String Sorting
letters = ("b", "g", "a", "d", "f", "c", "h", "e")
letters_sorted = sorted(letters)
print(letters_sorted)
