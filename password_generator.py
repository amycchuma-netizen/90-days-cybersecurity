import string
import secrets
print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
characters = string.digits +string.ascii_letters+string.punctuation

password=""
for i in range(12):
    password=password+ secrets.choice(characters)
print(password)
    



