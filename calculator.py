class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Can't divide by zero"

calc = Calculator()

res = calc.add(3, 9)
print("3 + 9 =", res)

res = calc.subtract(6, 2)
print("6 - 2 =", res)

res = calc.multiply(23, 3)
print("23 * 3 =", res)

res = calc.divide(144, 12)
print("144 / 12 =", res)

res = calc.divide(144, 0)
print("144 / 0 =", res)
