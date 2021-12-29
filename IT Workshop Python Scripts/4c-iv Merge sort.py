def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    # Creating temporary arrays and copying the elements to it
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
    # Merging the temporary arrays
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copying the remaining elements, if there are any left out
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


array = list(map(int, input('Enter the array of integers to be sorted(separated by spaces):').split()))
n = len(array)
print("Given array is")
print(*array)

merge_sort(array, 0, n - 1)
print("Sorted array is")
print(*array)
