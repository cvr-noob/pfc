def harmonic(n):
    if n<2:
        return 1
    return 1/n + harmonic(n-1)

a = int(input("Enter a number: "))
print(harmonic(a))
