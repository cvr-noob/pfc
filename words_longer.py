words = input("Enter any line: ").split(' ')
n = int(input("Enter a number: "))
myList = []

for word in words:
    if len(word) > n:
        myList.append(word)

print(f"The words that are longer than {n} are:", myList)
