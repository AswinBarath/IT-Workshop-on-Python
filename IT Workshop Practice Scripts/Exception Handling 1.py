try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print(x/y)
except ZeroDivisionError:
    print("Cannot be divided!")
except ValueError:
    print('Please enter integer values')
