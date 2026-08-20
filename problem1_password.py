# Problem 1: Password Length Validator

password = input("Enter your password: ")

# Check if the password is between 8 and 15 characters
if 8 <= len(password) <= 15:
    print("Password length is valid.")
else:
    print("Password too short or too long. Please try again.")
