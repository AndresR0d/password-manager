import unittest
import hashlib
import secrets
import string
from password_manager import (
    generate_password,
    add_password,
    view_websites,
    retrieve_password,
    passwords
)


class TestPasswordManager(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password()
        self.assertTrue(isinstance(password, str))
        self.assertEqual(len(password), 12)  # Default length is 12 characters

    def test_add_password(self):
        # Add a password entry
        add_password("example.com", "user123", "password123")

        # Check if the password entry exists in the dictionary
        self.assertIn("example.com", passwords)

    def test_view_websites(self):
        # Ensure the function returns a string
        self.assertTrue(isinstance(view_websites(), str))

    def test_retrieve_password(self):
        # Add a password entry
        add_password("example.com", "user123", "password123")

        # Retrieve the password for "example.com"
        result = retrieve_password("example.com")

        # Check if the result contains the expected information
        self.assertIn("Website: example.com", result)
        self.assertIn("Username/Email: user123", result)
        self.assertTrue(result.endswith("Password: " + hashlib.sha256("password123".encode()).hexdigest()))

    def test_retrieve_password_not_found(self):
        # Attempt to retrieve a password for a website that doesn't exist
        result = retrieve_password("nonexistent.com")
        self.assertEqual(result, "Website not found in password manager.")


if __name__ == "__main__":
    unittest.main()
