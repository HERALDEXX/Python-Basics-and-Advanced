'''Create a password generator function that suggests a password for a user that meets the requirements of having 8 characters has both numbers and letters and special characters.'''

import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

print(generate_password())