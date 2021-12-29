import numpy as np
import math as mp
arr1 = np.array([2, 8, 16])
arr2 = np.array([2, 8, 16])
res = arr1 + arr2
print(res)
res = np.array([mp.sqrt(i) for i in res])
print(res)
