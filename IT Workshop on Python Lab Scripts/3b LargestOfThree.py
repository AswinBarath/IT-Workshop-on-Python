print("Program to find the Largest of Three Numbers given")
print("Enter three numbers:")
largest = 0
a = int(input())
b = int(input())
c = int(input())
if a > c and a > b:
    largest = a
elif b > c:
    largest = b
else:
    largest = c
print("Largest of given three numbers is", largest)
