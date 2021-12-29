try:
    x = int(input("Enter a number:"))
    print(x/0)
except ZeroDivisionError as message:
    print("Exception type", type(message))
    print("exception type", message.__class__)
    print("Only Name", message.__class__.__name__)
    print("Message description:", message)
