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
string2 = client.recv(1024).decode()
occurences = {}
for i in range(len(string)):
    if string[i] == string2[i]:
        if string[i] not in occurences.keys():
            occurences[string[i]] = 1
        else:
            occurences[string[i]] += 1
try:
    maxChar = max(occurences, key=occurences.get)
    client.send(maxChar.encode())
    client.send(struct.pack("!I", occurences[maxChar]))
except ValueError:
    client.send(" ".encode())
    client.send(struct.pack("!I", 0))