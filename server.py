import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# AES-256 Key (32 bytes)
KEY = os.getenv("SECRET_KEY").encode()

# IV (16 bytes)
IV = b'1234567890123456'


def decrypt_message(enc_msg):
    # Decode Base64
    encrypted_data = base64.b64decode(enc_msg)

    # Create AES cipher
    cipher = AES.new(KEY, AES.MODE_CBC, IV)

    # Decrypt data
    decrypted = cipher.decrypt(encrypted_data)

    # Remove padding
    return unpad(decrypted, AES.block_size).decode('utf-8')


# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server
server_socket.bind(('localhost', 5000))

# Listen for connections
server_socket.listen(1)

print("Server listening on port 5000...")

# Accept connection
conn, addr = server_socket.accept()

print(f"Connected by {addr}")

# Receive encrypted data
data = conn.recv(1024)

print(f"Encrypted data received by server: {data.decode()}")

# Decrypt message
decrypted_text = decrypt_message(data.decode())

print(f"After Decryption message is: {decrypted_text}")

# Close connections
conn.close()
server_socket.close()