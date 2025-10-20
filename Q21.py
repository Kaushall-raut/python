import re

password = input("Enter your password: ")


if len(password) < 8:
    print("Weak Password,it should be 8 characters long")
elif not re.search(r"[A-Z]", password):
    print("Weak Password,it should contain atleast one capital letter")
elif not re.search(r"[a-z]", password):
    print("Weak Password,it should contain atleast one lower letter")
elif not re.search(r"\d", password):
    print("Weak Password")
elif not re.search(r"[@#$%&*]", password):
    print("Weak Password,is should contain atleast one special character")
else:
    print("Strong Password!")

