def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


array = list(map(int, input('Enter the array of integers to be sorted(separated by spaces):').split()))
insertion_sort(array)
print("Sorted array is:")
print(*array)
