
t, m = {}, []
a = list(map(int, input().split()))
b = int(input())
for i, j in enumerate(a):
    n = b - j
    if n in t:
        m.append(t[n] + i)
    t[j] = i
if m:
    m.sort()
    for k in m:
        print(k)
else:
    print("Not Found!")