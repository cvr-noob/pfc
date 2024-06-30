with open("sample", 'r') as file:
    words = file.read().split()

given = input("Enter word: ")
count = 0

for word in words:
    if word == given:
        count += 1

print(count)
