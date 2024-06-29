import re

def check_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least one number
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[$#@]', password):
        return False

    # Check for at least one lowercase letter and one uppercase letter
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # If all checks pass, return True
    return True

# Example usage:
password = input("Enter a password: ")
if check_password(password):
    print("Password is valid")
else:
    print("Password is invalid")
