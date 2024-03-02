
# INT: struct.pack("!I", number)
# STRING: string.encode()

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

integer = int(input("Please input an integer\n>>"))
s.send(struct.pack("!I", integer))
n = struct.unpack("!I", s.recv(4))[0]
for i in range(n):
    div = struct.unpack("!I", s.recv(4))[0]
    print(div)

