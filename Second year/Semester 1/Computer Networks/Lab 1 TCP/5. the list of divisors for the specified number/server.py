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
clients.append(client)
n = struct.unpack("!I", client.recv(4))[0]
divs = []
d = 1
while d < n//2:
    if not n%d:
        divs.append(d)
    d+=1
client.send(struct.pack("!I", len(divs)))
for i in divs:
    client.send(struct.pack("!I", i))
