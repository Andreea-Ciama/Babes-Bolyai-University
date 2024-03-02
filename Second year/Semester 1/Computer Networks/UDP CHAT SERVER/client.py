import socket
import threading
import os

UDP_IP = "192.168.0.143"
UDP_PORT = 5678
sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 

sock.sendto(b"connected", (UDP_IP, UDP_PORT))

def send():
    while True:
        MESSAGE = input().encode()
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def rec():
    while True:
        data, addr = sock.recvfrom(1024)
        print("%s:%s" %addr +" - " + data.decode())

s = threading.Thread(target = send)
r = threading.Thread(target = rec)

s.start()
r.start()