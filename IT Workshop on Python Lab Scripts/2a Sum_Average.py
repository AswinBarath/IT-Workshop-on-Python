print("Python Program to print the sum and average of natural numbers!")
limit = int(input("Enter the limit of numbers:"))
sumOfNumbers = (limit * (limit + 1)) / 2
averageOfNumbers = sumOfNumbers / limit
print("The sum of", limit, "natural numbers is", sumOfNumbers)
print("The Average of", limit, "natural number is", averageOfNumbers)