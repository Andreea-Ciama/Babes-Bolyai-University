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
n = client.recv(4)
n = struct.unpack("!I", n)[0]
first = []
for i in range(n):
    first.append(struct.unpack("!I", client.recv(4))[0])

common = []
m = struct.unpack("!I", client.recv(4))[0]
second = []
for i in range(m):
    num = struct.unpack("!I", client.recv(4))[0]
    second.append(num)
for i in first:
    if i not in second:
        common.append(i)
client.send(struct.pack("!I", len(common)))
for i in common:
    client.send(struct.pack("!I", i))

