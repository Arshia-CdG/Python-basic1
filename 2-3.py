def maghss(n):
    h = 0
    for i in range (1, n+1):
        if n % i == 0:
            h += i
    return h

def transform(n, c):
    a = []
    d = 0
    while n:
        n, r = divmod(n, c)
        a.append(str(r))
    for i in range (len(a)):
        d += int(a[len(a)- i - 1]) * (10 ** (len(a) - i - 1))
    return d

m = 0
u = 0
n, c = map(int,input().split( ))

while(n != -1 & c != -1):
    if 2 <= c <= 9:
        n = maghss(n)
        m += transform(n, c)
    else:
        u += 1
    n, c = map(int, input().split())
if u != 0:
    print("invalid base!")
else:
    print(m)
