import numpy as np

def value(letter):
    if letter.isupper():
        v = ord(letter) - ord('A')
    else:
        v = ord(letter) - ord('a')
    return v

def getLetter(integer):
    return chr(integer + ord('a'))

def mmi(a,m):
    inv = pow(a,-1,m)
    return inv

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def adjoint(k):
    n = k.shape[0]
    cofactor = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(k, i, axis=0), j, axis=1)
            cofactor[i, j] = ((-1) ** (i + j)) * round(np.linalg.det(minor))
    
    adj = cofactor.T

    for i in range(3):
        for j in range(3):
            adj[i,j] = int(adj[i,j]) % 26

    return adj

def KeyInverse(k):
    det = np.linalg.det(k)
    det = round(det)%26

    adj = adjoint(k)
    det = mmi(det,26)
    adj = adj*det
    k2 = np.empty((3,3))
    for i in range(3):
        for j in range(3):
            k2[i,j] = int(adj[i,j]) % 26

    return k2

def HillEncrpyt(plainText, k):
    cipherText = ""
    plainText = plainText.replace(" ", "")
    n = len(plainText)
    while(n%3 != 0):
        plainText+= 'x'
        n+=1

    for i in range(0, n, 3):
        p = np.empty((1,3))
        c = np.empty((1,3))
        for j in range(0,3):
            p[0,j] = value(plainText[i+j])
        
        c = np.dot(p,k)
        for j in range(0,3):
            x = getLetter(int(c[0,j]) % 26)
            cipherText += x
    
    return cipherText

def HillDecrpyt(cipherText, k2):
    plainText = ""
    n = len(cipherText)

    for i in range(0, n, 3):
        p = np.empty((1,3))
        c = np.empty((1,3))
        for j in range(0,3):
            c[0,j] = value(cipherText[i+j])

        p = np.dot(c,k2)
        for j in range(0,3):
            x = getLetter(int(p[0,j]) % 26)
            plainText += x 
    
    return plainText

def Key():
    while True:
        k = np.random.randint(1,51,size=(3,3))
        det = np.linalg.det(k)
        det = int(round(det)%26)

        if gcd(det,26) == 1:
            break
        else:
            continue

    return k
    
k = np.empty((3,3))
k = Key()

c = HillEncrpyt("Hello I am Mahad",k)
print(c)

k2 = np.empty((3,3))
k2 = KeyInverse(k)

print(HillDecrpyt(c,k2))
