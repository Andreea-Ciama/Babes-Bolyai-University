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
I = int(input("Please input the index\n>>"))
s.send(struct.pack("!I", I))
l = int(input("Please input the length\n>>"))
s.send(struct.pack("!I", l))
result = s.recv(1024).decode()
print("The substring is: " + result) 

