def sang_snt(n):
    mang_snt = [True] * (n+1)
    mang_snt[0] = mang_snt[1] = False
    count = 1
    for p in range(2,int(n**0.5)+1):
        print(p)
        if mang_snt[p] == True:
            for i in range(p*p,n+1,p):
                print(f"lan thu {count} {i}")
                mang_snt[i] = False
            count += 1
    prime_num = [i for i in range(2,n+1) if mang_snt[i]]
sang_snt(100)
