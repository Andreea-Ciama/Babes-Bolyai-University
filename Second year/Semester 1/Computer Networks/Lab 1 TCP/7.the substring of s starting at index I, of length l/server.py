import socket
import sys
import struct

PORT = 1234
clients = []


try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(5)
except socket.error as err:
    print(err.strerror)
    exit(-1)

client, addr = s.accept()
string = client.recv(1024).decode()
I = struct.unpack("!I", client.recv(4))[0]
l = struct.unpack("!I", client.recv(4))[0]
result = string[I:I+l]
client.send(result.encode())

