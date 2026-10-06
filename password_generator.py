import string
import secrets
import getpass
print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
characters = string.digits +string.ascii_letters+string.punctuation
password_length =int(input("Enter password length"))

password=""
for i in range(password_length):
    password=password+ secrets.choice(characters)
print(password)




