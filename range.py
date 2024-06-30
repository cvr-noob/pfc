def test_range(num):
    fn = int(input("Enter the 1st no. of the range: "))
    ln = int(input("Enter the last no. of the range: "))

    if num in range(fn, ln):
        print(num, "is in the given range")
    else:
        print(num, "is outside the given range")


n = int(input("Enter a number: "))
test_range(n)
