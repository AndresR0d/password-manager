import hashlib
import secrets
import string

# Define a dictionary to store passwords (You can use a dictionary for simplicity)
passwords = {}


# Function to generate a strong password
def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    # Generate characters based on complexity options
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))


# Function to add a new password entry
def add_password(website, username, password):
    if password == 'generate':
        password = generate_password()

    # Hash the password before storing it for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    passwords[website] = {
        'username': username,
        'password': hashed_password
    }


# Function to view all stored website names
def view_websites():
    if not passwords:
        return "No passwords stored."
    else:
        return "\n".join(passwords.keys())


# Function to retrieve a password
def retrieve_password(website):
    if website in passwords:
        username = passwords[website]['username']
        password = passwords[website]['password']
        return f"Website: {website}\nUsername/Email: {username}\nPassword: {password}"
    else:
        return "Website not found in password manager."
