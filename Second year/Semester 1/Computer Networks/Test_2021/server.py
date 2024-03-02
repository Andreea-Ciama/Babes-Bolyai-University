import socket
import threading
import random
import struct
import sys
import time

random.seed()
start=1; stop=2**17-1
my_num= random.randint(start,stop)
print('Server number: ',my_num)
mylock = threading.Lock()
client_guessed=False
winner_thread=0
e = threading.Event()
e.clear()
threads = []
client_count=0
number_of_digits = 0
digits = [int(d) for d in str(my_num)]

def countDigits(number):
    if number < 10:
        return 1
    else:
        return 1 + countDigits(number / 10)


def worker(cs):
    number_of_guessed_digits = 0
    global mylock, client_guessed, my_num, winner_thread, client_count,e
    my_idcount=client_count
    print('client #',client_count,'from: ',cs.getpeername(), cs)
    cs.sendall(struct.pack('!I', number_of_digits))

    while number_of_guessed_digits != len(digits):
        try:
            cnumber=cs.recv(4)
            cnumber=struct.unpack('!I',cnumber)[0]
            if cnumber in digits:
                number_of_guessed_digits += 1
                position = digits.index(cnumber)
                cs.sendall(struct.pack('!I', position))
            else:
                position = 0
                cs.sendall(struct.pack('!I', position))
        except socket.error as msg:
            print('Error:',msg.strerror)
            break

    if number_of_guessed_digits == len(digits):
        cs.sendall(b'W')
        print("We have a winner ", cs.getpeername())
        print("Thread ",my_idcount," winner")
        e.set()
    else: 
        cs.sendall(b'L')
        print("Thread ",my_idcount," looser")

    cs.close()
    print("Worker Thread ",my_idcount, " end")


def resetSrv():
    global mylock, client_guessed, winner_thread, my_num, threads,e, client_count
    while True:
        e.wait()
        for t in threads:
            t.join()
        print("all threads are finished now")
        e.clear()
        mylock.acquire()
        threads = []
        client_guessed = False
        winner_thread=-1
        client_count = 0
        my_num = random.randint(start,stop)
        print('Server number: ',my_num)
        mylock.release()

def main():
    global client_count, number_of_digits
    number_of_digits = countDigits(my_num)
    try:
        rs=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs.bind( ('0.0.0.0',1234) )
        rs.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    t=threading.Thread(target=resetSrv, daemon=True)
    t.start()
    while True:
        client_socket,addrc = rs.accept()
        t = threading.Thread(target=worker, args=(client_socket,) )
        threads.append(t)
        client_count+=1
        t.start()

main()