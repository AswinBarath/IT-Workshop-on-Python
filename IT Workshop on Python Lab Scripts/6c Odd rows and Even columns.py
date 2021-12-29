import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in range(0, a.shape[0]):
    if i % 2 != 0:
        print("Odd rows=", a[i])

for i in range(0, a.shape[1]):
    if i % 2 == 0:
        print("Even column :-")
        for j in range(0, a.shape[0]):
            print(a[j][i])
    print()
