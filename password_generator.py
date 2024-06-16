import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 12  # You can specify any length you need
password = generate_password(password_length)
print(f"Generated password: {password}")