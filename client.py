import socket
import json
import os

# IP address of the server
HOST = os.getenv("SERVER_HOST", "127.0.0.1")

# Port the server is listening on
PORT = 5000

# Request sent to the server
request = {
    "request": "system"
}

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

# Send the JSON request
client.send(json.dumps(request).encode())

# Receive the server's response
response = client.recv(1024).decode()

print(response)

# Close the connection
client.close()
