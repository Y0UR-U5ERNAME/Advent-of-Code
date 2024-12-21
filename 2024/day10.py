with open('input10.txt') as f:
    d = [list(map(int, i.strip())) for i in f.readlines()]

w = len(d[0])
h = len(d)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def path(i, j):
    n = d[j][i]
    if n == 9: return {(i, j)}
    c = set()
    for k in dirs:
        if 0 <= j + k[1] < h and 0 <= i + k[0] < w:
            if d[j + k[1]][i + k[0]] == n + 1:
                c |= path(i + k[0], j + k[1])
    return c

def path2(i, j):
    n = d[j][i]
    if n == 9: return 1
    c = 0
    for k in dirs:
        if 0 <= j + k[1] < h and 0 <= i + k[0] < w:
            if d[j + k[1]][i + k[0]] == n + 1:
                c += path2(i + k[0], j + k[1])
    return c

s = 0
s2 = 0
for j in range(h):
    for i in range(w):
        if d[j][i] == 0:
            s += len(path(i, j))
            s2 += path2(i, j)
print(s)
print(s2)