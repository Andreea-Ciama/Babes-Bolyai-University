import socket
import sys
import struct
import os
import threading
import random


PORT = 1234
clients = []
random.seed()
mynum = random.randint()
print("number is ", mynum)
mylock = threading.Lock()
found = False


def worker(client):
    while True:
        try:
            # do stuff
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