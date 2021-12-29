print("Python program to print Factorial of N given number")
n = int(input("Enter the Factorial number to be computed:"))


def factorial_of_n(num):
    fact = 1
    if num < 1:
        return fact
    else:
        for i in range(1, num+1):
            fact *= i
        return fact


print("Factorial of given number", n, "is", factorial_of_n(n))
