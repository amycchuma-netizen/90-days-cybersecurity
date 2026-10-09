print(list("abc"))
password = "123"
if len(password) < 6:
    raise ValueError("Password too short!")
try:
    password = "123"
    if len(password) < 6:
        raise ValueError("Password too short!")

except ValueError as e:
    print("Error:", e)



