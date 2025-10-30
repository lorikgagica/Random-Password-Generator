# Random Password Generator

import random, string
import os

# Step 1: Define Password Generation Function
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    # Character sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    # Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    # Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    # Shuffle the password to make it more random
    random.shuffle(password)
    # Convert the list to a string and return
    return ''.join(password)

# Step 2: User Interaction for multiple passwords
FILENAME = "passwords.txt"
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        pass

while True:
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        count = int(input("How many passwords to generate? "))
        passwords = []
        for _ in range(count):
            pwd = generate_password(length)
            print("Generated Password:", pwd)
            passwords.append(pwd)
        # Save all generated passwords to file
        with open(FILENAME, "a") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print(f"{count} password(s) saved to {FILENAME}.")
    except ValueError as e:
        print(e)
    again = input("Generate more? (y/n): ").strip().lower()
    if again != "y":
        print("Exiting Password Generator.")
        break