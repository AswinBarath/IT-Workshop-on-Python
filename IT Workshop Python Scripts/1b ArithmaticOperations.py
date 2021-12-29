print("Program to perform Arithmetic Operations")

iteration = True
number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

while iteration:
    operation = input("Choose an Arithmetic operator -> (+) (-) (*) (/) (%) :")
    if operation == "+":
        addition = number_1 + number_2
        print(number_1, " + ", number_2, " = ", addition)
    elif operation == "-":
        subtraction = number_1 - number_2
        print(number_1, " - ", number_2, " = ", subtraction)
    elif operation == "*":
        multiplication = number_1 * number_2
        print(number_1, " * ", number_2, " = ", multiplication)
    elif operation == "/":
        division = number_1 / number_2
        print(number_1, " / ", number_2, " = ", division)
    elif operation == "%":
        modulo = number_1 % number_2
        print(number_1, " % ", number_2, " = ", modulo)
    else:
        print("Wrong choice! Please try again!")
        continue
    another_operation = int(input("Want to perform another operation? Choose -> (1) (0):"))
    iteration = True if another_operation == 1 else False
