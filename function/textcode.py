from cryptography.fernet import Fernet

def encrypt_password(password):
    # Generate encryption key
    key = Fernet.generate_key()

    # Create Fernet object with key
    f = Fernet(key)

    # Encrypt password
    encrypted_password = f.encrypt(password.encode())

    # Save key and encrypted password to files
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    with open('password.bin', 'wb') as password_file:
        password_file.write(encrypted_password)

def decrypt_password(key_path, bin_path):
    # Read key from file
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

    # Create Fernet object with key
    f = Fernet(key)

    # Read encrypted password from file
    with open(bin_path, 'rb') as password_file:
        encrypted_password = password_file.read()

    # Decrypt password and return as string
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Encrypt password and save key and encrypted password to files
# encrypt_password('mysecretpassword')

# Decrypt password and print it
#password = decrypt_password('key.key', 'password.bin')
#print(password)
