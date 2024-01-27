def jam(x, y):
    while (y != 0):
        c = x & y
        x = x ^ y
        y = c << 1
    return x
v1 = int(input())
v2 = int(input())
a = int(input())
print(jam(v1, v2))
if (a == jam(v1, v2)):
    print("YES")
else:
    print("NO")