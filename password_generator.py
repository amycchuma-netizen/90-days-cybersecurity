import string
import secrets
from password_checker import check_password
characters = string.digits +string.ascii_letters +string.punctuation
while True :
    try:
        password_length =int(input("Enter password length greater than 4 :  "))
        if 4< password_length <64 :
            break
        else :
            print("Password is too small/large!")
    except ValueError:
        print("That's not a number!") 
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
check_password(final_p)




