first-input = int(input())
sevond-input = int(input())
l = bin(first-input ^ sevond-input)[2:]
changes = 0
for i in range (len(l)):
    if l[i] == "1":
        changes += 1
print (changes)
