b, a= map(int,input().split( ))
n = 0

if a >= b :
    for i in range(b, a + 1):
        m = 0
        for d in range(1, i + 1):
            if i % d == 0:
                m += 1
        if m == 2:
            n += 1
    print ("main order - amount: " + str(n))

if b > a:
    for i in range(a, b + 1):
        m = 0
        for d in range(1, i + 1):
            if i % d == 0:
                m += 1
        if m == 2:
            n += 1
    print ("reverse order - amount: " + str(n))
