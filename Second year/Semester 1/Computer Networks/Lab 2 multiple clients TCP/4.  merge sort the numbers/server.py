import socket
import sys
import struct
import os
import threading
import time

PORT = 1234
clients = []
N = 0
mylock = threading.Lock()
going = True
Numbers = []


def worker(client):
    global mylock, N, Numbers, going
    n = struct.unpack("!I", client.recv(4))[0]
    if n != 0:
        numbers = []
        for i in range(n):
            numbers.append(struct.unpack("!f", client.recv(4))[0])
        mylock.acquire()
        N += n
        Numbers += numbers
        mylock.release()
    else:
        mylock.acquire()
        going = False
        Numbers.sort()
        mylock.release()

    while going:
        continue
    client.send(struct.pack("!I", N))
    for number in Numbers:
        client.send(struct.pack("!f", number))
    time.sleep(1)
    client.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', PORT))
        s.listen(5)
    except socket.error as err:
        print(err.strerror)
        exit(-1)

    while going:
        client, addr = s.accept()
        if client not in clients:
            clients.append(client)
        t = threading.Thread(target=worker, args=(client,))
        t.start()