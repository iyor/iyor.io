"""
CLI tool used to calculate new usernames and password hashes
"""
from werkzeug.security import generate_password_hash

print("Please enter the new user: ")
user = input()
print("Please enter the new password: ")
password = input()

print("User hash: ")
print(generate_password_hash(user))
print("Password hash: ")
print(generate_password_hash(password))
