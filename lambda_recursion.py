n = int(input("Enter n: "))
res = lambda num: 0 if num < 1 else 1 + res(num // 2)
print(res(n))
