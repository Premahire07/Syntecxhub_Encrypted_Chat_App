# Secure Client-Server Communication using AES Encryption

A Python-based secure client-server communication system using TCP sockets and AES-256 encryption.  
This project demonstrates encrypted message transmission between a client and a server using the `pycryptodome` library.

---

## Features

- AES-256 Encryption
- TCP Socket Communication
- Secure Message Transmission
- Base64 Encoded Encrypted Messages
- Environment Variable Support using `.env`
- Simple and Beginner Friendly

---

## Technologies Used

- Python
- Socket Programming
- AES Encryption (CBC Mode)
- PyCryptodome
- Python-dotenv

---

## Project Structure

```text
project-folder/
│
├── client.py
├── server.py
├── .env
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

### 1 Clone Repository

```bash
git clone https://github.com/Premahire07/Syntecxhub_Encrypted_Chat_App
```

### 2 Move to Project Folder

```bash
cd Syntecxhub_Encrypted_Chat_App
```

### 3 Install Required Packages

```bash
pip install pycryptodome python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project folder.

```env
SECRET_KEY=your_32_byte_secret_key_here
```

---

## Run the Project

### Start Server

```bash
python server.py
```

### Start Client

Open another terminal and run:

```bash
python client.py
```

---

## Example Output

### Client Side

```text
Enter Message: Hello
Encrypted Message sent by client: q8xJHf9jLk...
```

### Server Side

```text
Server listening on port 5000...
Connected by ('127.0.0.1', 53214)
Encrypted data received by server: q8xJHf9jLk...
After Decryption message is: Hello
```

---


## Future Improvements

- Random IV Generation
- AES-GCM Mode
- File Encryption Support
- GUI Interface
- Secure Key Exchange
- Multi-client Communication

---

## Author

Prem Ahire

GitHub: https://github.com/Premahire07