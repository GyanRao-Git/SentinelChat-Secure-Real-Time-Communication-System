def password_validator(value:str):
    """
        validate password function for pydantic 
        input : password string
        output: valid password or error 
    """
    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long")

    upperCheck=lowerCheck=digitCheck=specialCheck=False
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

    for c in value:
        if c.isupper():
            upperCheck = True
        if c.islower():
            lowerCheck = True
        if c.isdigit():
            digitCheck=True
        if c in special_chars:
            specialCheck=True
        

    if not upperCheck:
        raise ValueError("There must be atleast one Uppercase character in password")
    
    if not lowerCheck:
        raise ValueError("There must be atleast one Lowercase character in password")
    
    if not digitCheck:
        raise ValueError("There must be atleast one Number in password")
    
    if not specialCheck:
        raise ValueError("There must be atleast one Special Character in password")
    
    return value