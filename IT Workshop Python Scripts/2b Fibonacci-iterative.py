print('Program to print N fibonacci numbers')
n = int(input("Enter the limit of fibonacci numbers:"))
a = 0
b = 1
print(a)
print(b)
for num in range(n - 2):
    c = a + b
    print(c)
    a = b
    b = c
