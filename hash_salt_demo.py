import hashlib
import os

# Create a dictionary to simulate a database holding username, hashed password, and salt
login_database = {}

def generate_salt():
    # Creating a random 16 byte salt
    # Without salting, if multiple users have the same password, 
    # they will have the same hash value, making it easier for attackers to identify such common passwords.
    return os.urandom(16)

def hashing_password_method(password, salt):
    # This method combines the password and salt and then hash them with SHA-256
    # Overview of what is happening:
    # .encode() converts a string into a sequence of bytes using a specified character encoding.
    # .sha256() computes the SHA-256 hash of the bytes.
    # .hexdigest() converts the resulting SHA-256 hash (which is binary data) into a hexadecimal string representation.
    combined = password.encode() + salt
    hashed_password = hashlib.sha256(combined).hexdigest()
    return hashed_password
    
def username_and_password_input():
    # This method prompts the user for their email (username) and password input, and returns these values.
    username = input('Enter your email: ')
    password = input('Enter your password: ')
    return username, password

def create_login_account():
    # This function create a login account.
    username, password = username_and_password_input()
    salt = generate_salt()
    hashed_password = hashing_password_method(password, salt)
    login_database[username] = [hashed_password, salt]
    
def login_attempt():
    # This function checks if user's detail exist
    username, password = username_and_password_input()
    if (username in login_database.keys()):
        # Checking if username exist in database
        user_hashed_password = login_database[username][0]
        user_salt = login_database[username][1]
        if (user_hashed_password == hashing_password_method(password, user_salt)):
            # Checking if password matches
            print('Login Successful!')
        else:
            print('Wrong Password')
    else:
        print("Username doesnt exist!")
        
while True:
    # Looping for user interaction
    choice = input("Enter 1 to create account, 2 to login or 0 to exit: ")
    if (choice == "1"):
        create_login_account()
    elif (choice == "2"):
        login_attempt()
    elif  (choice == "0"):
        break
    else:
        print("Invalid choice")
