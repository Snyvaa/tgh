def hoocne(pt,n,x):
    a = 0
    a = pt[0]**1+a
    d = []
    d.append(pt2[0])
    for i in range(1,n):
        a = pt[i] * x**i +a
    for i in range(0,n-1):
        d.append(x*d[i]+pt2[i+1])
    print(d)
    if a == 0 and d[-1] == 0:
        while d and d[-1] == 0:
            d.pop()
        n = len(d) - 1
        z = [
            f"{d[i]}x^{n - i}" if (n - i) > 0 else f"{d[i]}"  
            for i in range(len(d))
        ]
        if x < 0:
            in_ra = f"(x+{-x})" + "(" + " + ".join(z).replace("+ -", "- ") + ")"
        elif x > 0:
            in_ra = f"(x-{x})" + "(" + " + ".join(z).replace("+ -", "- ") + ")"
        else:
            in_ra = f"(x)" + "(" + " + ".join(z).replace("+ -", "- ") + ")"
        print(in_ra)
    else:
        return False
    
pt = [2,0,0,1,-3] #từ trái sang phải 2x^3+x^2-3 thì ghi [2,1,0,-3]
pt2 = pt.copy()
pt.reverse()
n = len(pt)
x = 1
hoocne(pt,n,x)
