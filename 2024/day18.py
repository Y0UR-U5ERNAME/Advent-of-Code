with open('input18.txt') as f:
    l = [list(map(int, i.split(','))) for i in f.readlines()]

w = 71
p = (0, 0)

m = [[-1 for j in range(w)] for i in range(w)]
for i in range(len(l)):
    c = l[i]
    m[c[1]][c[0]] = i

from collections import deque
for n in range(1024, len(l) + 1):
    good = False
    o = deque()
    o.append((p[0], p[1], 0))
    v = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    out = None
    while len(o):
        x = o.popleft()
        if x[:2] in v: continue
        if x[:2] == (w-1, w-1):
            if n == 1024: print(x[2])
            good = True
            break
        for i in dirs:
            nx = x[0] + i[0]
            ny = x[1] + i[1]
            if not(0 <= nx < w and 0 <= ny < w): continue
            if -1 < m[ny][nx] < n: continue
            if (nx, ny) in v: continue
            o.append((nx, ny, x[2] + 1))
        v.add(x[:2])
    if not good:
        print(l[n - 1])
        break