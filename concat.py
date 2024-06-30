myList = ['p', 'q']
new = []
n = int(input("Enter range: "))
for i in range(1, n + 1):
    for j in myList:
        new.append(j + str(i))
print(new)
