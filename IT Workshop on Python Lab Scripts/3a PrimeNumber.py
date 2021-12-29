n, m, i, j, flag = 0, 0, 0, 0, 0

print("Enter lower limit of the interval:", end=" ")
n = int(input())

print("Enter upper limit of the interval:", end=" ")
m = int(input())

print("Prime numbers between", n, "and", m, "are:", end=" ")

for i in range(n, m + 1):
    if i == 1:
        continue
    # flag = 1 means i is prime
    flag = 1

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            # flag = 0 means i is not prime
            flag = 0
            break

    if flag == 1:
        print(i, end=" ")
