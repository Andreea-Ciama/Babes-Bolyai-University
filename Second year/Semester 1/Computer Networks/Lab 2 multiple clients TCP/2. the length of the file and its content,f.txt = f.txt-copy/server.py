import json
import socket
import os
from _thread import *


# CONNECT MULTIPLE CLIENTS
# connects every client from the various addresses
# provided by the server simultaneously
def multi_thread_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server received the path: ' + data.decode('utf-8')
        path = data.decode('utf-8')
        if not data:
            break

        if os.path.exists(path):
            with open(str(path)) as f:
                content = f.readlines()
                length = len(f.readlines())
            package = json.dumps(
                {
                    "content": content,
                    "length": length
                }
            )
        else:
            package = json.dumps(
                {
                    "content": "",
                    "length": -1
                }
            )

        connection.sendall(str.encode(package))
    connection.close()


if __name__ == "__main__":
    # prep phase
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 420
    thread_count = 0

    # connect the HOST and PORT to socket server
    # listening to the connection from the client side
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening...')
    server_socket.listen(5)

    # ACCEPT CLIENT SOCKET CONNECTION
    while True:
        client, address = server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_thread_client, (client, ))
        thread_count += 1
        print('Thread number: ' + str(thread_count))

    server_socket.close()
