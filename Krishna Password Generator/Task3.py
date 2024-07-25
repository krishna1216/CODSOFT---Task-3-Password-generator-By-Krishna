import random
import string

def getpassword(length):   
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation      
    characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    pass_length = int(input("Enter the length of the password you want to generate: "))
    if pass_length <= 0:
        raise ValueError("Password length should be greater than zero.")
except ValueError as ve:
    print(f"Error: {ve}")
else:
    # Generate and print the password
    generated_password = getpassword(pass_length)
    print(f"Generated password of length {pass_length}: {generated_password}")
