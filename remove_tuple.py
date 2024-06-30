l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Original list:", l)

l = [t for t in l if t]
print("After removing empty tuples, list is:", l)
