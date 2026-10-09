from datetime import datetime
with open("login.txt") as file :
    for line in file:
        parts = line.strip().split(",")
            #here we check whether the ID is a digit
        if parts[0].isdigit():
            print("Valid ID")
        else:
            print("Invalid ID")
            