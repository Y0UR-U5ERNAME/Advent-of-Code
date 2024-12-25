with open('input23.txt') as f:
    l = [i.strip().split('-') for i in f.readlines()]

con = {}
for i in l:
    if i[0] not in con: con[i[0]] = []
    con[i[0]].append(i[1])
    if i[1] not in con: con[i[1]] = []
    con[i[1]].append(i[0])

s = set()
for i in con:
    if i[0] != 't': continue
    c = con[i]
    for j in range(len(c)-1):
        for k in range(j+1, len(c)):
            if c[j] in con[c[k]]:
                s.add(tuple(sorted((i, c[j], c[k]))))
print(len(s))

mx = {}
for i in con:
    sofar = {i}
    for j in con[i]:
        if j not in sofar:
            if set(con[j]) & sofar == sofar:
                sofar |= {j}
    if len(sofar) > len(mx): mx = sofar
print(','.join(sorted(mx)))