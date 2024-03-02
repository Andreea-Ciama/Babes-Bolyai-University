import socket
import struct
import random
import sys
import time

def main():
    sv_addr = input("Enter address: ")
    port = int(input("Enter port: "))
    N = int(input("Enter number of seconds: "))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sv_addr, port))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    guessed_positions = 0
    min = 0
    max = 9
    random.seed()

    number_of_digits = s.recv(4)
    number_of_digits = struct.unpack('!I', number_of_digits)[0]

    print("The number of digits is ", str(number_of_digits))
    
    
    while guessed_positions != number_of_digits:
        digit = random.randint(min, max)
        try:
            s.sendall(struct.pack('!I', digit))
            answer = s.recv(4)
            answer = struct.unpack('!I', answer)[0]
        except socket.error as msg:
            print("Error: ", msg.strerror)
            s.close()
            exit(-2)
        print("Sent ", str(digit), " Position: ", str(answer))
        if answer != 0:
            guessed_positions += 1

    win = s.recv(1)
    win = win.decode('ascii')
    if win == b'W':
        print("I won!")
    else:
        print("I lost")

    s.close()

main()