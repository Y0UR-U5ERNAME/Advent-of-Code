with open('input5.txt') as f:
    d = f.readlines()

i = d.index('\n')
s1 = [list(map(int, j.split('|'))) for j in d[:i]]
s2 = [list(map(int, k.split(','))) for k in d[i+1:]]

s = 0
for i in s2:
    good = True
    for k in s1:
        if k[0] in i and k[1] in i and i.index(k[0]) > i.index(k[1]):
            good = False
            break
    if good: s += i[len(i) // 2]
print(s)

s = 0
for i in s2:
    good = False
    bad = False
    while not good:
        good = True
        for k in s1:
            if k[0] in i and k[1] in i and (i1:=i.index(k[0])) > (i2:=i.index(k[1])):
                good = False
                bad = True
                i[i1], i[i2] = i[i2], i[i1]
    if bad: s += i[len(i) // 2]
print(s)