b = bin(int(input()))[2:]
a = bin(int(input()))[2:]
s = [0] * 64
for i in range(len(a)):
    s[i + 32 - len(a)] = a[i]
for i in range(len(b)):
    s[i + 64 - len(b)] = b[i]
m = int(input())
s2 = [0] * m
for i in range(m):
    n = int(input())
    if s[64 - n - 1] == "1":
        s2[i] = "yes"
    else:
        s2[i] = "no"
for i in range (m):
    print(s2[i])