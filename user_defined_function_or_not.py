from types import FunctionType, LambdaType


def func():
    return 1


print(isinstance(func, FunctionType))
print(isinstance(func, LambdaType))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, LambdaType))

print(isinstance(max, FunctionType))
print(isinstance(max, LambdaType))

print(isinstance(abs, FunctionType))
print(isinstance(abs, LambdaType))
