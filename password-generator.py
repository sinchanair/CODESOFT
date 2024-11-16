import random
import string

def generate_password(length):
    # Define all possible characters (lowercase, uppercase, digits, and special)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = int(input("Enter the password length: "))
password = generate_password(length)
print("Generated password:", password)