print('Program to print N fibonacci numbers, recursively')


def fibonacci(n):
    if n <= 0:
        print("Incorrect input")

    elif n == 1:
        return 0

    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the limit of fibonacci numbers:"))
for num in range(1, n+1):
    print(fibonacci(num))
