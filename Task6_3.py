# Lesson 6: Python Strings
# 3. Interactive Help Desk Bot

def parse_command(user_input):
    predefined_commands = ["help", "issue", "contact support"]

    for command in predefined_commands:
        if command in user_input.lower():
            print(f"Response related to the '{command}' command goes here.")
            return

    print("No predefined command found in the input.")

def categorize_issue(user_input):
    if "issue" in user_input.lower():
        keywords = ["login", "performance", "error", "other"]

        for keyword in keywords:
            if keyword in user_input.lower():
                print(f"Category of the issue: {keyword.capitalize()}")
                return

    print("No issue category found in the input.")

# Example usage
user_input = input("Enter your text input: ")
parse_command(user_input)

user_issue_description = input("Describe the issue: ")
categorize_issue(user_issue_description)
