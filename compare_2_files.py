import filecmp

f1 = 'f1.txt'
f2 = 'f2.txt'

res = filecmp.cmp(f1, f2)
if res == True:
    print("The files are identical")
else:
    print("The files are not identical")
