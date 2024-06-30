from functools import reduce

l = eval(input("Enter a list of numbers: "))

sum = reduce(lambda x, y: x + y, l)
print("Sum of the values in the list is:", sum)
