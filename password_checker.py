from getpass import getpass
def check_password(password):
    common_passwords = ["password","iloveyou","thisismypassword1#","icancreate123#"]
    score =0
    length= len(password)
    if length >= 12:
        print("Long enough")
        score= score+1
    else :
        print("Password is too short")
    has_number = False  
    has_uppercase = False
    has_lowercase = False  
    has_symbol = False
    for char in password :
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase =True
        if not char.isalnum():
            has_symbol= True                     
    if has_number == True:
        print("Has a number")
        score= score+1
    else:
        print("Add a number")
        
    if has_uppercase == True:
        print("Has uppercase")
        score= score+1
    else: 
        print("Needs an uppercase letter")
        
    if has_lowercase == True:
        print("Has lowercase")
        score= score+1
    else:
        print("Needs a lowercase letter")
    if has_symbol == True :
        print("Has a symbol")
        score= score+1
    else:
        print("Add a symbol")
    if password.lower() in common_passwords :
        print("This is a very common password")
        print("Weak Password")
    else:
        if score==5 :
            print("Strong Password")
        elif score>=3 :
            print("Medium Password")
        else :
            print("Weak Password")
            
if __name__ == "__main__":
       password = getpass("Enter password-")
       check_password(password)