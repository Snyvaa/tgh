def Prime_factors(N):
    factors = []
    i = 2
    while i*i<=N:
        if N%i:
            print("1 ",N%i)
            i+=1
        else:
            N//=i
            factors.append(i)
    if N>1:
        factors.append(N)
    return factors
Prime_factors(10)
