def encryption(m, n):
    # c = (m^2) mod n
    c = (m * m) % n
    return c

def mod(k, b, m):
    i = 0
    a = 1
    v = []
    while k > 0:
        v.append(k % 2)
        k = (k - v[i]) // 2
        i += 1
    for j in range(i):
        if v[j] == 1:
            a = (a * b) % m
            b = (b * b) % m
        else:
            b = (b * b) % m
    return a

def modulo(a, b):
    return a % b if a >= 0 else (b - abs(a % b)) % b

def extendedEuclid(a, b):
    if b > a:
        a, b = b, a
    i, j, x, y = 0, 1, 1, 0
    while b != 0:
        q = a // b
        temp1 = a % b
        a, b = b, temp1
        temp2 = i
        i, x = x - q * i, temp2
        temp3 = j
        j, y = y - q * j, temp3
    return [x, y, 1]

def decryption(c, p, q):
    r = mod((p + 1) // 4, c, p)
    s = mod((q + 1) // 4, c, q)

    arr = extendedEuclid(p, q)
    rootp = arr[0] * p * s
    rootq = arr[1] * q * r
    r1 = modulo((rootp + rootq), n)

    if r1 < 128:
        return r1

    negative_r = n - r1
    if negative_r < 128:
        return negative_r

    s1 = modulo((rootp - rootq), n)
    if s1 < 128:
        return s1

    negative_s = n - s1
    return negative_s

if __name__ == "__main__":
    # private key pair(p,q) of the form 3 mod 4
    p, q = 10930102054568426764504043452559325790475583848895190436950515749179531193863, 73825450128289294440037105389758552820176082758249063485471228049565279165991

    # public key n
    n = p * q

    # vector for storing the encrypted message
    e = []

    # vector for storing the decrypted message
    d = []

    message = "Hello!"
    print("Plain text:", message)

    for i in range(len(message)):
        e.append(encryption(ord(message[i]), n))

    print("Encrypted text:", "".join(map(str, e)))

    for i in range(len(e)):
        d.append(decryption(e[i], p, q))

    print("Decrypted text:", "".join(map(chr, d)))

