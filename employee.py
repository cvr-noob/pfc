fp = open('employee.txt', 'r')

count = 0
for line in fp:
    count += 1

print("No. of employees are:", count)
