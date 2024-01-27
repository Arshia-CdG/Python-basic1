import math
def sum2():
    s = 0
    while(True):
        n = input()
        if n == 'end':
            break
        s += int(n)
    print(s)
def average2():
    s = 0
    s1 = 0
    while(True):
        n = input()
        if n == 'end':
            break
        s1 += 1
        s += int(n)
    print(round((s / s1), 2))
def max2():
    s1 = int(input())
    while (True):
        n = input()
        if n == 'end':
            break
        s1 = max(s1, int(n))
    print(s1)
def min2():
    s1 = int(input())
    while (True):
        n = input()
        if n == 'end':
            break
        s1 = min(s1, int(n))
    print(s1)
def lcme(a, b):
    return (a * b) // math.gcd(a, b)
def lcd2():
    x = int(input())
    while(True):
        n = input()
        if n == 'end':
            break
        x = lcme(x, int(n))
    print(x)
def gcd2():
    x = int(input())
    while(True):
        n = input()
        if n == 'end':
            break
        x = math.gcd(x, int(n))
    print(x)
f = input()
if f == 'sum':
    sum2()
elif f == 'average':
    average2()
elif f == 'lcd':
    lcd2()
elif f == 'gcd':
    gcd2()
elif f == 'min':
    min2()
elif f == 'max':
    max2()
else:
    print('Invalid command')