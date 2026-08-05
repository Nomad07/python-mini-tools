import random
import string

length = 12

characters = string.ascii_letters + string.digits
password = ""

for _ in range(length):
    password += random.choice(characters)

print("Generated password:", password)
