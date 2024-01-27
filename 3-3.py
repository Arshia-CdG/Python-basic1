i = 0
b = list(input())
while len(b) > i:
    if b[i] == '@':
        j = i + 1
        while len(b) > j:
            if b[j] == '#':
                b.pop(j)
                break
            else:
                j += 1
        i += 1
    else:
         i += 1
m = '' . join(b)
m = ' ' . join(m.split())
m = m . replace("\\n", "\n")
m = m . replace("\\t", "\t")
print(f"Formatted Text: {m}")