def sum_series(n):
    if n == 0:
        return 0
    return n + sum_series(n - 2)


n = int(input("Enter n: "))
print(f"The sum series upto {n} terms is {sum_series(n)}")
