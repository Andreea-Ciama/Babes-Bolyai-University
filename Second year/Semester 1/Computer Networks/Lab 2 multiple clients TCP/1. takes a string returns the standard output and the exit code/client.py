# INT: struct.pack("!I", number)
# STRING: string.encode()

import socket
import struct
import sys


IP = 'localhost'
PORT = 1235

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
except socket.error as err:
    print(err.strerror)
    exit(-1)

while True:
    string = input("Please give a command\n>>")
    s.send(string.encode())
    output = s.recv(1024).decode()
    print(output)

