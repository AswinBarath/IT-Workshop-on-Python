def binary_search(arr, x):
    begin = 0
    end = len(arr) - 1
    mid = 0
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] < x:
            begin = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return mid
    return -1


array = list(map(int, input('Enter the sorted array of integers seperated by spaces:').split()))
item = int(input('Enter the integer to be searched:'))
result = binary_search(array, item)
print(f'The integer number {item} is present at index {result}') if result != -1 else print(f'Sorry, the integer {item} is not found')
