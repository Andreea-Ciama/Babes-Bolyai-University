import socket
IP = 'localhost'
PORT = 1234


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'message', (IP, PORT))