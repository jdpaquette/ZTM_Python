# AGE CALCULATOR
# birth_year = int(input("What year were you born? "))
# age = 2021 - birth_year
# print(f"You are {age} years old!")

# PASSWORD CHECKER
user_name = input("Please enter your username: ")
password = input("Please enter your password: ")

secret = "*" * len(password)

print(f"Hello {user_name}, your password {secret} is {len(password)} characters long!")