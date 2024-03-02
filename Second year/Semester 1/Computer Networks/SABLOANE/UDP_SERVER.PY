import socket

PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PORT))

while True:
    data, addr = sock.recvfrom(1024) 