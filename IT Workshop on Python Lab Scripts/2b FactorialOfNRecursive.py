print("Python program to print Factorial of N given number")
n = int(input("Enter the Factorial number to be computed:"))


def factorial_of_n(num):
    if num < 1:
        return 1
    else:
        return num * factorial_of_n(num - 1)


print("Factorial of given number", n, "is", factorial_of_n(n))
