with open('file.txt', 'w') as file:
    file.write("""Hello World
    Eswar""")

fp = open('file.txt', 'r')
l = 0
w = 0
for line in fp:
    w += len(line.split())
    l += 1
print(f'The file has {l} lines and {w} words')
fp.close()
