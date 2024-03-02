import socket
import struct
import sys
from random import randint

IP = 'localhost'
PORT = 7777

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
except socket.error as err:
    print(err.strerror)
    exit(-1)

for i in range(100):
    x = randint(-100, 100)
    s.send(struct.pack("!f", x))
    y = randint(-100, 100)
    s.send(struct.pack("!f", y))

string = s.recv(1024)
print(string.decode())
