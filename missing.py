l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = ['d', 'e', 'f', 'g', 'h']
print("Missing values in l2: ", ''.join(set(l1).difference(l2)))
print("Additional values in l2: ", ''.join(set(l2).difference(l1)))
