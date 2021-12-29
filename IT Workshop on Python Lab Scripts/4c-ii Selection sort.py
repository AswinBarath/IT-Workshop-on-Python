array = list(map(int, input('Enter the array of integers to be sorted(separated by spaces):').split()))
for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print("Sorted array is:")
print(*array)
