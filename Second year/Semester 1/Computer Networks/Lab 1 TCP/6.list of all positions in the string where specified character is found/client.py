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

string = input("Please input the string\n>>")
s.send(string.encode())
char = input("Please input the character\n>>")
s.send(char.encode())
n = struct.unpack("!I", s.recv(4))[0]
for i in range(n):
    print(struct.unpack("!I", s.recv(4))[0])
