def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
print(f"GCD of {a} and {b} is {gcd(a, b)}")
