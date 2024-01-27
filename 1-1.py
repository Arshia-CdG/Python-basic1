x = int(input())
v = int(input())
l = bin(x ^ v)[2:]
d = 0
for i in range (len(l)):
    if l[i] == "1":
        d += 1
print (d)