f1 = open('s1.txt', 'r')
m1 = f1.read()
f1.close()
f2 = open('s2.txt', 'r')
m2 = f2.read()
f2.close()

with open('new_file.txt', 'w') as f3:
    f3.write(m1)

with open('new_file.txt', 'a') as f3:
    f3.write("\n"+m2)

with open('new_file.txt', 'r') as f3:
    print(f3.read())
