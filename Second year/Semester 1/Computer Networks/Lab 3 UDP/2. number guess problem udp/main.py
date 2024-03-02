import socket
import random
import struct
import time
import sys

IP = 'localhost'
PORT = 1236

lower = 1
upper = 2 ** 17 - 1
random.seed()
finished = False

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print("Error: ", msg.stderror)
    exit(-1)

while not finished:
    time.sleep(0.2)
    number = random.randint(lower, upper)
    print("Number is ", number)
    try:
        s.sendto(struct.pack("!I", number), (IP, PORT))
        answer, _ = s.recvfrom(1)
    except socket.error as msg:
        print("Error: ", msg.stderror)
        s.close()
        exit(-2)
    if answer == b'H':
        print("Server sent H")
        lower = number
    elif answer == b'L':
        print("Server sent L")
        upper = number
    elif answer == b'G' or answer == b'W':
        finished = True

if answer == b'W':
    print("Congratulations, you won!!")
else:
    print("You lost!")