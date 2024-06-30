f1 = open('s1.txt', 'r')
f2 = open('s2.txt', 'r')

f11 = f1.read()
f21 = f2.read()
ftemp = f21

print("File 1:\n"+f11)
print("File 2:\n"+f21)
f1.close()
f2.close()

f1 = open('s1.txt', 'w')
f2 = open('s2.txt', 'w')

f2.write(f11)
f1.write(ftemp)
f1.close()
f2.close()

f1 = open('s1.txt', 'r')
f2 = open('s2.txt', 'r')

print("After exchanging,")
print("File 1:\n"+f1.read())
print("File 2:\n"+f2.read())
f1.close()
f2.close()
