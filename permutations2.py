from itertools import permutations

n = permutations(eval(input("Enter numbers as a list: ")))
print("The possible permutations are:")
for i in n:
    print(i)
