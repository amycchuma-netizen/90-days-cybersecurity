import string
import secrets
characters = string.digits +string.ascii_letters +string.punctuation
password_length =int(input("Enter password length  "))
password=""
password = password + secrets.choice(string.ascii_uppercase)
password = password + secrets.choice(string.punctuation)
password = password + secrets.choice(string.ascii_lowercase)
password = password + secrets.choice(string.digits)
for i in range(password_length-4):
    password=password+ secrets.choice(characters)
preferred =list(password)
secrets.SystemRandom().shuffle(preferred)
final_p="".join(preferred)
print(final_p)





