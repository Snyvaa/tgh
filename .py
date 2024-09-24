import math
def hh(n):
    tong = 1
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            tong += i
            if i != n//i:
                tong += n//i
    return tong == n
def prime(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            return False
    return True
def pp(n):
    for p in range(2,600):
        if prime(p):
            if prime(2**p-1):
                print((2**p-1) * (2**(p-1)))
                if (2**p-1) * (2**(p-1)) == n:
                    return True
    return False
pp(402924829242920202949220546754675468756785698402924829242920202949220546754675468756785698402924829242920202949220546754675468756785698)
