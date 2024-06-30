from itertools import permutations

chars = ['a', 'e', 'i', 'o', 'u']
per = permutations(chars)
for i in per:
    print(''.join(i), end=' ')
