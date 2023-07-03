def powMod(a, b, m):
    return (a**b) % m

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def Devide(a, b):
    return a // b, a % b

def Extended_Euclid(r0, r1):
    s = [1, 0]
    t = [0, 1]
    r = [r0, r1]
    q = [0]
    i = 0
    while True:
        res = Devide(r[i], r[i + 1])
        r.append(res[1])
        q.append(res[0])
        if i >= 2:
            s.append(s[i - 2] - q[i - 1] * s[i - 1])
            t.append(t[i - 2] - q[i - 1] * t[i - 1])
        if res[1] == 0:
            t.append(t[i - 1] - q[i] * t[i])
            break
        i+=1
    ans = t[-1]
    return ans if ans >= 0 else ans + 26