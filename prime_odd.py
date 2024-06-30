odds = set([x*2+1 for x in range(1, 10)])
print(odds)

primes = set()
for num in range(2, 20):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.add(num)
print(primes)

print("Union:", odds.union(primes))
print("Intersection:", odds.intersection(primes))
print("Symmetric Difference:", odds.symmetric_difference(primes))
print("Difference:", odds.difference(primes))
