# CODSOFT Internship - Task 3
# Password Generator (Command Line Version)
# Created by: Manthan Prajapati

import random
import string

def generate_password(length):
    """Generate a random password of the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("          PASSWORD GENERATOR")
    print("====================================")

    try:
        # Get user input for password length
        length = int(input("Enter the desired password length: "))

        # Check for minimum valid length
        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
