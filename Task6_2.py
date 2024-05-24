# Lesson 6: Python Strings
# 2. User Input Data Processor

def validate_name(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name must be at least 2 characters long.")
    else:
        print("Names are valid!")

def check_password_complexity(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_uppercase and has_lowercase and has_digit):
        print("Error: Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
    else:
        print("Password meets complexity requirements!")

def format_email(email):
    formatted_email = email.lower().replace(" ", "")
    if "@" not in formatted_email:
        print("Error: Invalid email format. Please include an '@' symbol.")
    else:
        print(f"Formatted email: {formatted_email}")

# Example usage
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
validate_name(user_first_name, user_last_name)

user_password = input("Enter your password: ")
check_password_complexity(user_password)

user_email = input("Enter your email address: ")
format_email(user_email)
