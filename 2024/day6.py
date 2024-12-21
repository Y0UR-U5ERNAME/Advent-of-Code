with open('input6.txt') as f:
    d = f.readlines()

w = len(d[0]) - 1
h = len(d)

m = om = [list(i[:-1]) for i in d]

for i in range(w):
    for j in range(h):
        if m[j][i] == '^':
            g = og = (i, j)

dir = (0, -1)

s = 0
while True:
    if m[g[1]][g[0]] != 'X':
        m[g[1]][g[0]] = 'X'
        s += 1
    n = (g[0] + dir[0], g[1] + dir[1])
    if not(0 <= n[0] < w and 0 <= n[1] < h): break
    if m[n[1]][n[0]] == '#':
        dir = (-dir[1], dir[0])
        n = (g[0] + dir[0], g[1] + dir[1])
    else: g = n
print(s)

'''
pm = [i.copy() for i in m.copy()]

s = 0
m = [i.copy() for i in om.copy()]
for i in range(w):
    for j in range(h):
        if i == og[0] and j == og[1]: continue
        if pm[j][i] != 'X': continue
        g = og
        dir = (0, -1)
        m[j][i] = '#'

        seen = {}
        while True:
            if g in seen and seen[g] == dir:
                s += 1
                break
            seen[g] = dir

            n = (g[0] + dir[0], g[1] + dir[1])
            if not(0 <= n[0] < w and 0 <= n[1] < h): break
            if m[n[1]][n[0]] == '#':
                dir = (-dir[1], dir[0])
                n = (g[0] + dir[0], g[1] + dir[1])
            else: g = n
        m[j][i] = '.'
print(s)
'''

def p2(m, g, dir, seen={}, placed=False):
    s = 0
    new = {}
    while True:
        if (g in seen and seen[g] == dir) or (g in new and new[g] == dir):
            s += 1
            break
        odir = dir

        n = (g[0] + dir[0], g[1] + dir[1])
        if not(0 <= n[0] < w and 0 <= n[1] < h): break
        while m[n[1]][n[0]] == '#':
            turn = True
            dir = (-dir[1], dir[0])
            n = (g[0] + dir[0], g[1] + dir[1])
        
        if not placed and n not in new:
            m[n[1]][n[0]] = '#'
            s += p2(m, g, dir, new, True)
            m[n[1]][n[0]] = '.'
        
        new[g] = odir
        g = n
    return s
print(p2(om, og, (0, -1)))