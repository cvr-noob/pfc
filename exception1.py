a = ['python', 'exceptions', 'try and except']

try:
    for i in range(4):
        print(f"a[{i}] = {a[i]}")
except IndexError:
    print("Index out of range")
