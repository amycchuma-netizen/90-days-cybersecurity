import string
import secrets
print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
characters = string.digits +string.ascii_letters +string.punctuation
password_length =int(input("Enter password length  "))

password=""
password = password + secrets.choice(string.ascii_uppercase)
password = password + secrets.choice(string.punctuation)
password = password + secrets.choice(string.ascii_lowercase)
password = password + secrets.choice(string.digits)
for i in range(password_length-4):
    password=password+ secrets.choice(characters)
print(password)




