import socket
import json
from datetime import datetime
import random
import platform

# Listen on all available network interfaces
HOST = "0.0.0.0"

# Port used by the server
PORT = 5000

# Sample responses for the motivation request
quotes = [
    "Keep building cool stuff.",
    "Small progress is still progress.",
    "Every bug teaches something."
]

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the server to restart without waiting for the port to be released
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the host and port
server.bind((HOST, PORT))

# Start listening for incoming client connections
server.listen()

print(f"Server listening on port {PORT}")

try:
    while True:
        # Wait for a client to connect
        conn, addr = server.accept()

        print(f"Connection from {addr}")

        # Receive data from the client
        data = conn.recv(1024).decode()

        # Convert the JSON request into a Python dictionary
        request = json.loads(data)

        # Return the current server date and time
        if request["request"] == "time":
            response = {
                "response": str(datetime.now())
            }

        # Return information about the server environment
        elif request["request"] == "system":
            response = {
                "hostname": platform.node(),
                "os": platform.system(),
                "release": platform.release(),
                "architecture": platform.machine()
            }

        # Return a random motivational quote
        elif request["request"] == "motivation":
            response = {
                "message": random.choice(quotes)
            }

        # Handle invalid request types
        else:
            response = {
                "error": "Unknown request"
            }

        # Convert the response to JSON and send it to the client
        conn.send(json.dumps(response).encode())

        # Close the connection after responding
        conn.close()

except KeyboardInterrupt:
    print("\nShutting down server...")

finally:
    # Release the socket when the server exits
    server.close()