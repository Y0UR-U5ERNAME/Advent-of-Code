from math import ceil

with open('input2.txt') as f:
    count = 0
    count2 = 0
    for i in f.readline().split(','):
        low, high = map(int, i.split('-'))
        L1 = len(str(low))
        L2 = len(str(high))
        for L in range(L1, L2 + 1):
            if L == 1: continue
            added = set()
            for l in range(L // 2, 0, -1):
                if L % l != 0: continue
                n = sum(10 ** k for k in range(0, L, l))
                nlow = max(10**(l-1), ceil(low / n)) * n
                nhigh =  min(10**l-1, high // n) * n
                toadd = 0
                for j in range(nlow, nhigh + 1, n):
                    if j not in added:
                        toadd += j
                        added.add(j)
                if L / 2 == l: count += toadd
                count2 += toadd

print(count)
print(count2)