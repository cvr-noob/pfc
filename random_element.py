import os
import random

print("Random elements from list:")
l = [1, 2, 3, 4, 5]
print(random.choice(l))
print(random.choice(l))

print("Random elements from set:")
s = {1, 2, 3, 4, 5}
print(random.choice(tuple(s)))
print(random.choice(tuple(s)))

print("Random values from dictionary:")
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(random.choice(tuple(d.values())))
print(random.choice(tuple(d.values())))

print("Random files from a directory:")
print(random.choice(os.listdir('/')))
print(random.choice(os.listdir('/etc')))
