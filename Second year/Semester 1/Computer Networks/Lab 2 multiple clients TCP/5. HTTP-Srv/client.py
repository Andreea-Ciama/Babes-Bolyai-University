
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

address = input("Please input the address\n>>")
s.send(address.encode())
output = s.recv(4096).decode()
print(output)