def is_valid_password(password):
    # Check for minimum length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        return False

    # Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        return False

    # If all checks pass
    return True




# Test cases
print(is_valid_password("Passw0rd"))  # Expected output: True
print(is_valid_password("password"))  # Expected output: False
print(is_valid_password("PASSWORD"))  # Expected output: False
print(is_valid_password("P@ssw0rd"))  # Expected output: True

"""
To complete this exercise:
--------------------------
Implement the 'is_valid_password' function to check if the provided password meets the required criteria. 
The criteria include having a minimum length of 8 characters, containing at least one uppercase letter, 
and at least one lowercase letter.

Exercise Breakdown:
-------------
The .lower() and .upper() methods can convert a given string to lower or upper case, respectively. 

name = "John"
print(name.upper())   # JOHN is printed
 
"""
