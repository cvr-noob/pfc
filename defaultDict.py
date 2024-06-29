from collections import defaultdict

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 2, 3]

temp = defaultdict(set)

for k, v in zip(letters, numbers):
    temp[k] = v

print(dict(temp))
