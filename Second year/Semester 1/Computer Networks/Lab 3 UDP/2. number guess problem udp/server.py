import socket
import random
import struct
import sys

PORT = 1236
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

random.seed()
start=1; stop=2**17-1
my_num= random.randint(start,stop)
print('Server number: ',my_num)
going = True
clients = []
winner = None
while going:
    data, addr = sock.recvfrom(4)
    if addr not in clients:
        clients.append(addr)
    number = struct.unpack("!I", data)[0]
    if number > my_num:
        sock.sendto(b'L', addr)
    elif number < my_num:
        sock.sendto(b'H', addr)
    else:
        going = False
        winner = addr
        sock.sendto(b'W', addr)

for client in clients:
    if client != winner:
        sock.sendto(b'G', client)