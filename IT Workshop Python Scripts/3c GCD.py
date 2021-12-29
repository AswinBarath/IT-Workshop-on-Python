def gcd(m, n):
    if m < n:
        m, n = n, m

    while m % n != 0:
        m, n = n, m % n
    return n


print("Program to find GCD of two number!")
print("Enter two numbers to calculate gcd:-")
a = int(input())
b = int(input())
print("GCD of", a, "and", b, "is", gcd(a, b))
