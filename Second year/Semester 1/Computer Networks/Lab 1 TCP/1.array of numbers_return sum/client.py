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
c = s.recv(4)
c = struct.unpack("!I", c)
print("The sum is "+ str(c[0]))

#struct package documentation for data types
