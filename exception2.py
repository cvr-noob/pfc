class InvalidAgeException(Exception):
    """Raised when age is less than 18"""
    pass

try:
    age = int(input("Enter age: "))
    if age<18:
        raise InvalidAgeException
    else:
        print("Eligible to vote!")
except InvalidAgeException:
    print("Age is too young!")
