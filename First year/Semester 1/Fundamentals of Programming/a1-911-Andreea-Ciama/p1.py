#Generate the first prime number larger than n (natural)
def prim(x):
    """
    purpose -> Check if a number is prime
    :param x -> The number we will check
    :return -> 1 if x is prime or 0 if it's not
    """
    if x == 0 or x == 1:
        return 0
    else:
        for d in range(2,x//2+1,1):
            if x%d==0:
                return 0
    return 1

def read():
    n= input("n=")
    n= int(n)
    return n

def solve():
    """
    purpose -> find the first prime number larger than n
    :return -> the first prime number larger than n
    """
    n= read()
    ok=0
    while ok==0:
        n=n+1
        if prim(n)==1:
            ok=1
    print (n)

solve()