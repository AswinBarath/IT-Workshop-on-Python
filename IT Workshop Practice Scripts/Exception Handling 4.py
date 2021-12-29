try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print(x/y)
# try:
#     fl = open("text.txt", 'r')
#     # fl = open("text.txt", 'w')
#     fl.write('Information written here')
except (ZeroDivisionError, IOError, ValueError) as message:
    print("Exception type", type(message))
    print("Exception class name", message.__class__)
    print("Exception Message description:", message)
