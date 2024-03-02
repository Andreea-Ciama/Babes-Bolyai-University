import socket
import sys
import struct

PORT = 1234
clients = []


try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(5)
except socket.error as err:
    print(err.strerror)
    exit(-1)

client, addr = s.accept()
string = client.recv(1024).decode()
count = 0
for char in string:
    if char == ' ':
        count+=1
client.send(struct.pack("!I", count))
