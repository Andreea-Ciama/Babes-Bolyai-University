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
sum = 0
for i in range(n):
    num = struct.unpack("!I", client.recv(4))[0]
    sum+=num
client.send(struct.pack("!I", sum))
