from collections import deque

def bitprint(x, size):
    for j in range(size[1]-1, -1, -1):
        for i in range(size[0]-1, -1, -1):
            print('#' if x & (1 << (i + j * size[0])) else '.', end='')
        print()
    print()

def solve(bitrep, pres, size, idx=0):
    if len(pres) == idx: return True
    ps = bs[idx]
    if bitrep == 0: # only these checks are needed for actual input
        if sum(i * ps[0].bit_count() for i in pres) > size[0] * size[1]: return False
        if sum(pres) <= (size[0] // 3) * (size[1] // 3): return True
    if pres[idx] == 0: return solve(bitrep, pres, size, idx + 1)
    if bitrep.bit_count() + pres[idx] * ps[0].bit_count() > size[0] * size[1]: return False
    poss = {}
    for c, shape in enumerate(ps):
        for y in range(size[1] - 3 + 1):
            for x in range(size[0] - 3 + 1):
                shifted = shape << (x + y * size[0])
                if not (bitrep & shifted): poss[(x, y, c)] = shifted
    if len(poss) < pres[idx]: return False
    opn = deque()
    opn.append((0, bitrep))
    cls = set()
    while opn:
        x, r = opn.pop()
        if x == pres[idx]:
            if solve(r, pres, size, idx + 1): return True
        toadd = deque()
        c = 0
        for i in poss:
            if r & poss[i]: continue
            newr = r | poss[i]
            c += 1
            if newr in cls: continue
            toadd.append((x + 1, newr))
        if x + c >= pres[idx]: opn.extend(toadd)
        cls.add(r)
    return False

with open('input12.txt') as f:
    count = 0
    shapes = []
    b = f.read().split('\n\n')
    for i in b[:-1]:
        s = i.split('\n')[1:]
        toadd = set()
        for x in 0, 1:
            for y in 0, 1:
                toadd.add(tuple(tuple(s[2-i if x else i][2-j if y else j] == '#' for j in range(3)) for i in range(3)))
                toadd.add(tuple(tuple(s[2-j if y else j][2-i if x else i] == '#' for j in range(3)) for i in range(3)))
        shapes.append(toadd)
    for i in b[-1].split('\n'):
        w = i.split(' ')
        size = tuple(map(int, w[0][:-1].split('x')))
        p = tuple(map(int, w[1:]))
        bs = [[sum(k[l][m] << (m + l * size[0]) for l in range(3) for m in range(3)) for k in j] for j in shapes]
        count += solve(0, p, size)

print(count)