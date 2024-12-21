with open('input16.txt') as f:
    m = [list(i.strip()) for i in f.readlines()]

w = len(m[0])
h = len(m)

S = next((i, j) for i in range(w) for j in range(h) if m[j][i] == 'S')
E = next((i, j) for i in range(w) for j in range(h) if m[j][i] == 'E')

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)] # must be in this order

d = []
v = []
d.append((*S, dirs[3], 0, None)) # x, y, (dx, dy), score, parent index in v
best = None
btiles = {d[0]}
vd = {}
inf = float('inf')
while len(d):
    mn = inf
    idx = 0
    for c, i in enumerate(d):
        if i[3] < mn:
            mn = i[3]
            p = i
            idx = c
    d.pop(idx)
    if best != None and p[3] > best: break
    if p[:2] == E:
        if best == None:
            print(p[3])
            best = p[3]
        curr = (p[0], p[1], p[4])
        while curr[2] != None:
            btiles.add(curr[:2])
            curr = v[curr[2]]
    else:
        for D in dirs:
            if p[2] == (-D[0], -D[1]): continue
            nx = p[0] + D[0]
            ny = p[1] + D[1]
            score = p[3] + (1 if D == p[2] else 1001)
            if m[ny][nx] == '#': continue
            if (nx, ny, (-D[0], -D[1])) in vd or (nx, ny, D) in vd and vd[(nx, ny, D)] <= score: continue
            d.append((nx, ny, D, score, len(v)))
    v.append((p[0], p[1], p[4]))
    vd[p[:3]] = p[3]
print(len(btiles))