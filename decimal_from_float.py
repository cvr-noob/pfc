from decimal import Decimal

print("From float:")
pi = Decimal(3.14159)
print(pi)
print(pi.as_tuple())

num = Decimal("123.25")
print(num)
print(num.as_tuple())
