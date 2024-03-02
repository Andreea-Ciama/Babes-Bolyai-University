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

n = int(input("Please input the array \n n= "))
res = s.send(struct.pack("!I", n))

for i in range(n):
    num = int(input(">> "))
    s.send(struct.pack("!I", num))

n = int(input("Please input the array \n n= "))
res = s.send(struct.pack("!I", n))

for i in range(n):
    num = int(input(">> "))
    s.send(struct.pack("!I", num))


n = s.recv(4)
n = struct.unpack("!I", n)[0]
for i in range(n):
    print(struct.unpack("!I", s.recv(4))[0])


