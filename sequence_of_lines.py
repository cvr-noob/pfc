lines = []

# Reading input
while True:
    text = input()
    if text:
        lines.append(text)
    else:
        break

# Displaying
for line in lines:
    print(line.lower())
