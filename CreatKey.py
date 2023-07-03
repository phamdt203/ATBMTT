import Math

def getN(p, q):
    return p * q

def getPhi(p, q):
    return (p - 1) * (q - 1)

def getA(b, phi):
    return Math.Extended_Euclid(phi, b)

def key_generate(p, q, b):
    n = getN(p, q)
    phi = getPhi(p, q)
    a = getA(b, phi)
    pubKey = [b, n]
    priKey = [a, b, q]
    return pubKey, priKey