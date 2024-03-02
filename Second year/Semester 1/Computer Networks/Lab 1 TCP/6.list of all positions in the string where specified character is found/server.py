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
char = client.recv(1).decode()
l = []
for i in range(len(string)):
    if string[i] == char:
        l.append(i)
client.send(struct.pack("!I", len(l)))
for i in l:
    client.send(struct.pack("!I", i))

