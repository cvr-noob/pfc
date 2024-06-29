from math import factorial

def coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def pattern(n):
    for i in range(n):
        print(' '*(n-i-1), end='')
        for j in range(i+1):
            print(coeff(i, j), end=' ')
        print()

a = int(input("Enter a number: "))
pattern(a)
