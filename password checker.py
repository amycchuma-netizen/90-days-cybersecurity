password = input("Enter password-")
length= len(password)
if length >= 12:
    print("Long enough")
else :
    print("Password is too short")
has_number = False  
has_uppercase = False
has_lowercase = False  
for char in password :
    if char.isdigit():
        has_number = True
    if char.isupper():
                has_uppercase = True
    if char.islower():
                        has_lowercase =True
if has_number == True:
    print("Has a number")
else:
    print("Add a number")
    
if has_uppercase == True:
    print("Has uppercase")
else: 
    print("Needs an uppercase letter")
    
if has_lowercase == True:
    print("Has lowercase")
else:
    print("Needs a lowercase letter")