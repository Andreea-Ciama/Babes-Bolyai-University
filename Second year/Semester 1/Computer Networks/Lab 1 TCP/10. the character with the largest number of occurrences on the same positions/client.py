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
string2 = input("Please input the second string\n>>")
s.send(string2.encode())
char = s.recv(1).decode()
n = struct.unpack("!I", s.recv(4))[0]
print("Character " + char + " appears " + str(n) + " times.")