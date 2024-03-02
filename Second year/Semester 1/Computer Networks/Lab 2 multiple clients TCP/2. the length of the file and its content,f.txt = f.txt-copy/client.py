import json
import os.path
import socket

# 2. The client sends the complete path to a file. The server returns back the length of the file and its content in
# the case the file exists. When the file does not exist the server returns a length of -1 and no content. The client
# will store the content in a file with the same name as the input file with the suffix –copy appended (ex: for f.txt
# => f.txt-copy).

if __name__ == "__main__":
    client_socket = socket.socket()
    host = '127.0.0.1'
    port = 420

    # create connection with the server
    print('Waiting for connection response')
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))

    # connecting the clients
    res = client_socket.recv(1024)
    while True:
        i = input('> ')
        client_socket.send(str.encode(i))
        res = client_socket.recv(1024)
        data = json.loads(res.decode())
        file_content = data.get("content")
        file_length = data.get("length")
        file_name = os.path.basename(i)
        file_name = file_name + "-copy"

        with open(file_name, 'w') as f:
            f.writelines(str(file_content))

        print(f"The content of the file is in {file_name} and this is the content:\n")
        f1 = open(file_name, 'r')
        c = f1.read()
        f1.close()
        print(c)

    client_socket.close()
