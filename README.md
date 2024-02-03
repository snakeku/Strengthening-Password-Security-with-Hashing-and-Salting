# Strengthening-Password-Security-with-Hashing-and-Salting
This Python script demonstrates secure password storage techniques using SHA-256 hashing and salting. It provides an extra layer of security by hashing passwords before storing them in a database.

By using SHA-256 hashing and salting, you ensure that even if the database is compromised, attackers will only have access to hashed and salted versions of the passwords, making it significantly more challenging for them to retrieve the original passwords. 

## Features
SHA-256 Hashing: Passwords are securely hashed using the SHA-256 cryptographic hash function.
Salting: Unique salts are generated for each user's account, preventing identical passwords from having the same hash.
User Interaction: Users can create accounts and log in via a simple command-line interface.
Database Simulation: User account information, including hashed passwords and salts, is simulated using a Python dictionary.
