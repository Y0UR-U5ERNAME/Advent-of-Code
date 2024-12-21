from math import log, ceil

with open('input11.txt') as f:
    d = list(map(int, f.read().strip().split()))

for n in (25, 75):
    l = {}
    for i in d:
        if i not in l: l[i] = 0
        l[i] += 1

    for i in range(n):
        lc = l.copy()
        for a in lc:
            b = lc[a]
            l[a] -= b
            if a == 0:
                if 1 not in l: l[1] = 0
                l[1] += b
            elif (L:=int(1 + log(a, 10))) % 2 == 0:
                L = int(1 + log(a, 10))
                left = a // (10 ** (L//2))
                right = a % (10 ** (L//2))
                if left not in l: l[left] = 0
                if right not in l: l[right] = 0
                l[left] += b
                l[right] += b
            else:
                if a*2024 not in l: l[a*2024] = 0
                l[a*2024] += b
    print(sum(l.values()))
    print({l[i] for i in l if l[i]})