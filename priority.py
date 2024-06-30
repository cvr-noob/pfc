def check(op1, op2):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    if priority[op1] > priority[op2]:
        print(f"{op1} has higher priority than {op2}")
    elif priority[op1] < priority[op2]:
        print(f"{op2} has higher priority than {op1}")
    else:
        print(f"{op1} and {op2} have equal priority")


op1 = input("Enter op1: ")
op2 = input("Enter op2: ")
check(op1, op2)
