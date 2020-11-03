import string
import random

print("-------------- PASSWORD GENERATOR ----------------")

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

password_quantity = int(input("Enter the number of passwords you want --> "))

password_length = int(input("How long do you want your password(s) to be --> "))

print("Your passwords are: ")

for i in range(password_quantity):
    password = ''
    for j in range(password_length):
        password += random.choice(chars)
    print(password)

print("Enjoy your extra security!")