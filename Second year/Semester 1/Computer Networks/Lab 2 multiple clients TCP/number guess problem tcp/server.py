import socket
import random
import time

# Generate a random float number <SRF> for the server
SRF = random.uniform(0.0, 1.0)

# Create a socket and set it up for server listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)  # Listen for up to 5 client connections

clients = []

try:
    while True:
        print("Waiting for connections...")
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {client_address}")

        # Set a timeout for waiting for incoming connections
        server_socket.settimeout(10)

        if len(clients) == 1:
            start_time = time.time()

        if len(clients) > 1 and (time.time() - start_time) >= 10:
            # Calculate closest client's guess
            closest_client = min(clients, key=lambda c: abs(float(c.recv(1024)) - SRF))
            for client in clients:
                if client == closest_client:
                    client.send(f"You have the best guess with an error of {SRF - float(client.recv(1024))}".encode())
                else:
                    client.send("You lost !".encode())

            # Close all connections
            for client in clients:
                client.close()
            break

except socket.timeout:
    # Handle timeout (no connections received within 10 seconds)
    print("No connections received within 10 seconds")

finally:
    server_socket.close()
