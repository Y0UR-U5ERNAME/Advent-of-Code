with open('input20.txt') as f:
    l = f.readlines()

w = len(l[0].strip())
h = len(l)

S = next((c, d) for d, j in enumerate(l) for c, i in enumerate(j) if i == 'S')
E = next((c, d) for d, j in enumerate(l) for c, i in enumerate(j) if i == 'E')

m = [list(i.strip()) for i in l]

from collections import deque
o = deque()
oxy = {}
o.append((S[0], S[1], 0)) # x, y, score
v = {}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
sc = [[None for j in i] for i in l]
while len(o):
    x = o.popleft()
    sc[x[1]][x[0]] = x[2]
    if x[:2] == E:
        print(x[2])
        break
    for i in dirs:
        nx = x[0] + i[0]
        ny = x[1] + i[1]
        if l[ny][nx] == '#':
            continue
        if (nx, ny) in v: continue
        o.append((nx, ny, x[2] + 1))
    v[x[:2]] = x[2]

s = 0
for i in range(1, w-1):
    for j in range(1, h-1):
        if m[j][i] != '#': continue
        if '#' not in (m[j-1][i], m[j+1][i]):
            s += abs(sc[j-1][i] - sc[j+1][i]) >= 100 + 2
        if '#' not in (m[j][i-1], m[j][i+1]):
            s += abs(sc[j][i-1] - sc[j][i+1]) >= 100 + 2
print(s)

s = 0
coun = {}
M = [i.copy() for i in m.copy()]
for i in range(1, w-1):
    for j in range(1, h-1):
        if sc[j][i] == None: continue
        for K in range(20+1):
            if i + K >= w-1: continue
            for L in range(-20+K, 20-K+1):
                if K == 0 and L > 0: continue
                if not(1 <= j + L < h-1): continue
                if sc[j+L][i+K] == None: continue
                d = abs(sc[j][i] - sc[j+L][i+K]) - K - abs(L)
                if d not in coun: coun[d] = 0
                coun[d] += 1
                s += abs(sc[j][i] - sc[j+L][i+K]) >= 100 + K + abs(L)
print(s)