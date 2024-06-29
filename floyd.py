n = int(input("Enter no. of rows: "))
temp = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(temp, end='\t')
        temp+=1
    print()
