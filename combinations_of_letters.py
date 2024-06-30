from itertools import product

d = {
    '1': ['a', 'b'],
    '2': ['c', 'd']
}

values = d.values()
comb = list(product(*values))
for i in comb:
    print(''.join(i))
