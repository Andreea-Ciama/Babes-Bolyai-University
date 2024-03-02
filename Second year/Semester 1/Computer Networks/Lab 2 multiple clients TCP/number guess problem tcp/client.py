import socket
import random

# Generate a random float number <CRF> for the client
CRF = random.uniform(0.0, 1.0)

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Send the client's guess to the server
client_socket.send(str(CRF).encode())

# Receive and print the server's response
response = client_socket.recv(1024).decode()
print(response)

# Close the client connection
client_socket.close()
