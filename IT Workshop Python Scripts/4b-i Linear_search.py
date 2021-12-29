def linear_search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


array = list(map(int, input('Enter the array of integers seperated by spaces:').split()))
item = int(input('Enter the integer to be searched:'))
result = linear_search(array, item)
print(f'The integer number {item} is present at index {result}') if result != -1 else print(f'Sorry, the integer {item} is not found')
