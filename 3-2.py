import re
n = int(input())
m = set()
for i in range(n):
    d = input()
    if '@' in d:
        h = r"@([A-Za-z0-9.-]+\.[A-Za-z0-9.-]+)"
        s = re.findall(h, d)
        m.add(s[0])
a = sorted(m)
for i in (a):
    print(i)