l = [10, 20, 30, 40, 50]
print("Original list is:", l)

value = int(input("Enter value to insert: "))
index = int(input("Enter index to insert: "))

l.insert(index, value)
print("After inserting, the list is:", l)
