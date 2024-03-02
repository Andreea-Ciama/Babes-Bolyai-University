import socket
import struct
import sys

IP = 'localhost'
PORT = 1234

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
except socket.error as err:
    print(err.strerror)
    exit(-1)

n = int(input("Please input n\n>>"))
s.send(struct.pack("!I", n))
for i in range(n):
    num = float(input(">>"))
    s.send(struct.pack("!f", num))
N = struct.unpack("!I", s.recv(4))[0]
for i in range(N):
    print(struct.unpack("!f", s.recv(4))[0])
