import socket
import threading
import os


port = 5678

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', port))

clients = []

def rec():
    while True:
        data, addr = server.recvfrom(1024)
        if addr not in clients: 
            clients.append(addr)
        print("%s:%s" %addr +" - " + data.decode())
        for client in clients:
            if client != addr:  
                server.sendto(data, client)


def send():
    while True:
        MESSAGE = input().encode()
        for client in clients:
            server.sendto(MESSAGE, client)

r = threading.Thread(target = rec)
r.start()
s = threading.Thread(target = send)
s.start()
 