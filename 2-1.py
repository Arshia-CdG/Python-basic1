a = int(input())
for i in range(1, a + 1): 
    for j in range(0, a - i + 1): 
        print(end='') 
    b = 1 
    for j in range(1, i + 1):
        if j == i:
            print("1")
        else:
            print(b , " " ,sep='',end='')
        b = b * (i - j) // j 
    print()

