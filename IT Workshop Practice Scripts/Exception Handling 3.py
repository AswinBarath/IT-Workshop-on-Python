try:
    fl = open("text.txt", 'r')
    # fl = open("text.txt", 'w')
    fl.write('Information written here')
except IOError:
    print("File is missing bro!")
else:
    print("Information is written inside the file bro!")
