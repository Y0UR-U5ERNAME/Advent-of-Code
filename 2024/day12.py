from sys import setrecursionlimit

with open('input12.txt') as f:
    d = [list(i.strip()) for i in f.readlines()]

w = len(d[0])
h = len(d)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def fill(x, y, m):
    p = d[y][x]
    m[y][x] = 1
    out = (1, 0) # area, perimeter
    neighbors = 0
    for i in dirs:
        nx = x + i[0]
        ny = y + i[1]
        if not(0 <= nx < w and 0 <= ny < h): continue
        if d[ny][nx] == p:
            neighbors += 1
            if m[ny][nx] == 1: continue
            f = fill(nx, ny, m)
            out = (out[0] + f[0], out[1] + f[1])
    return (out[0], out[1] + 4 - neighbors)

m = [[0 for j in range(w)] for i in range(h)]
s = 0
for i in range(w):
    for j in range(h):
        if m[j][i] == 1: continue
        f = fill(i, j, m)
        s += f[0] * f[1]
print(s)

setrecursionlimit(1500)

d = [[d[i // 2][j // 2] for j in range(2 * w)] for i in range(2 * h)]
w = len(d[0])
h = len(d)

def fill2(x, y, m):
    p = d[y][x]
    m[y][x] = 1
    out = (1, 0) # area, sides
    neighbors = 0
    for c, i in enumerate(dirs):
        nx = x + i[0]
        ny = y + i[1]
        if not(0 <= nx < w and 0 <= ny < h): continue
        if d[ny][nx] == p:
            neighbors |= 1 << c
            if m[ny][nx] == 1: continue
            f = fill2(nx, ny, m)
            out = (out[0] + f[0], out[1] + f[1])
    return (out[0], out[1] +
        (neighbors in (0b1100, 0b0110, 0b0011, 0b1001)
        or (neighbors==0b1111 and any(0<=x+i[0]<w and 0<=y+i[1]<h and d[y+i[1]][x+i[0]]!=p for i in [(1, 1), (1, -1), (-1, -1), (-1, 1)])))
    )

m = [[0 for j in range(w)] for i in range(h)]
s = 0
for i in range(w):
    for j in range(h):
        if m[j][i] == 1: continue
        f = fill2(i, j, m)
        s += f[0] // 4 * f[1]
print(s)