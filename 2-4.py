n = int(input())
d = {}
i = 0
m = 0
while(True):
    s = input()
    if s == 'B':
        m += 1
    if s == 'END':
        break
    d[i] = s
    i += 1
duck = [[0 for i in range(n)] for j in range(m + 1)]
duck[0][0] = 1
ofogh = 0
amood = 0
for i in range(i):
    if d[i] == 'R':
        ofogh += 1
        if ofogh > n - 1:
            ofogh = n - 1
        duck[amood][ofogh] = 1
    elif d[i] == 'B':
        amood += 1
        duck[amood][ofogh] = 1
    elif d[i] == 'L':
        ofogh -= 1
        if ofogh < 0:
            ofogh = 0
        duck[amood][ofogh] = 1
for i in range(m + 1):
    for j in range(n):
        if duck[i][j] == 1:
            if j != n - 1:
                print('* ', end='')
            else:
                print('*')
        else:
            if j != n - 1:
                print('. ', end='')
            else:
                print('.')
if ofogh != n - 1:
    print("There's no way out!")