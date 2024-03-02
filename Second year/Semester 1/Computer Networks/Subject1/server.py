import socket
import sys
import struct

PORT = 7777

clients = []

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(5)
except socket.error as err:
    print(err.strerror)
    exit(-1)

client, addr = s.accept()
clients.append(client)
for i in range(100):

    n = client.recv(4)
    x = struct.unpack("!f", n)[0]
    n = client.recv(4)
    y = struct.unpack("!f", n)[0]

string="The current approximation of PI is 3.14 using 1000 samples"

client.send(string.encode())
