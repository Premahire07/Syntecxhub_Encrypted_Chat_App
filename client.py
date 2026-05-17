import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# AES-256 Key (32 bytes)
KEY = os.getenv("SECRET_KEY").encode()

# IV (16 bytes)
IV = b'1234567890123456'


def encrypt_message(msg):
    # Create AES cipher
    cipher = AES.new(KEY, AES.MODE_CBC, IV)

    # Encrypt message with padding
    encrypted = cipher.encrypt(
        pad(msg.encode('utf-8'), AES.block_size)
    )

    # Convert to Base64
    return base64.b64encode(encrypted).decode('utf-8')


# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 5000))

# User input
message = input("Enter Message: ")

# Encrypt message
encrypted_msg = encrypt_message(message)

# Print encrypted message
print(f"Encrypted Message sent by client: {encrypted_msg}")

# Send encrypted message
client_socket.sendall(encrypted_msg.encode())

# Close socket
client_socket.close()