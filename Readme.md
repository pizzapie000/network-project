Overview
As a software engineer, I am building my understanding of computer networking and systems. I wanted to build a client-server application that demonstrates how software can communicate across a network using TCP sockets and JSON messages. This project allowed me to gain experience with socket programming, network communication, and processing data between two computers.

This software is built up of a Python server application and a Python client application. The server runs on an Ubuntu virtual machine hosted in Proxmox and listens for incoming TCP connections. The client runs on a separate computer and sends requests to the server. The server processes each request and returns a JSON response.

To use the software:

Start the server program by running:
python3 server.py
Set the `SERVER_HOST` environment variable to the server's IP address. If it is
not set, the client uses `127.0.0.1`.

Windows PowerShell:

```powershell
$env:SERVER_HOST = "server-ip-address"
```

Linux/macOS:

```bash
export SERVER_HOST="server-ip-address"
```

Run the client program:

python client.py
Modify the request value in the client to test different server functions.
Supported requests include:

time – Returns the current date and time from the server.
system – Returns information about the server's operating system.
motivation – Returns a randomly selected motivational message.
The purpose of writing this software was to learn how client-server applications communicate across a network and how TCP sockets and JSON can be used to exchange information between systems.

Software Demo Video: https://youtu.be/G8ikJNp_0ZM

Network Communication
This project uses a client-server architecture.

The server runs continuously and waits for incoming connections. A client connects to the server, sends a JSON request, receives a JSON response, and then disconnects.

The application uses:

Protocol: TCP
Port: 5000
Messages are transmitted using JSON format.

Example request:

{
    "request": "time"
}
Example response:

{
    "response": "2026-10-28 14:35:12"
}
Example system information response:

{
    "hostname": "ubuntu-docker",
    "os": "Linux",
    "release": "6.14.0-29-generic",
    "architecture": "x86_64"
}
The server processes incoming requests and generates responses based on the request type.

Development Environment
Tools used:

Visual Studio Code
Ubuntu Server Virtual Machine
Proxmox Virtual Environment
Windows 11
Python 3.13
Programming Language:

Python
Libraries Used:

socket
json
datetime
random
platform
All libraries used are included in Python's standard library.

Useful Websites
https://docs.python.org/3/library/socket.html
https://docs.python.org/3/library/json.html
https://docs.python.org/3/library/platform.html
https://realpython.com/python-sockets/
Future Work
Add a graphical user interface for the client application.
Allow multiple clients to connect simultaneously using threading.
Expand the server to retrieve real-time system statistics such as memory usage, CPU utilization, and uptime.
