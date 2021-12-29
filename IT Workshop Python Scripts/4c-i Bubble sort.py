def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = list(map(int, input('Enter the array of integers to be sorted(separated by spaces):').split()))
bubble_sort(array)

print("Sorted array is:")
print(*array)
