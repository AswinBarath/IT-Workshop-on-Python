try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print(x/y)
except BaseException as message:
    print("Exception type", type(message))
    print("exception type", message.__class__)
    print("Message description:", message)
