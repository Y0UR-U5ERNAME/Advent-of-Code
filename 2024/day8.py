with open('input8.txt') as f:
    d = [list(i)[:-1] for i in f.readlines()]

w = len(d[0])
h = len(d)

ant = []
for i in range(w):
    for j in range(h):
        if d[j][i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            ant.append((i, j, d[j][i]))

s = 0
for i in range(w):
    for j in range(h):
        br = False
        for k in range(len(ant) - 1):
            for l in range(k + 1, len(ant)):
                a1 = ant[k]
                a2 = ant[l]
                if a1[2] != a2[2]: continue
                dx1 = (a1[0] - a2[0])
                dy1 = (a1[1] - a2[1])
                dx2 = (a1[0] - i)
                dy2 = (a1[1] - j)
                if (dx1 == -dx2 and dy1 == -dy2) or (2 * dx1 == dx2 and 2 * dy1 == dy2):
                    s += 1
                    br = True
                    break
            if br: break
print(s)

inf = float('inf')
s = 0
for i in range(w):
    for j in range(h):
        br = False
        for k in range(len(ant) - 1):
            for l in range(k + 1, len(ant)):
                a1 = ant[k]
                a2 = ant[l]
                if a1[2] != a2[2]: continue
                if (i, j) in ((a1[0], a1[1]), (a2[0], a2[1])):
                    s += 1
                    br = True
                    break
                dx1 = (a1[0] - a2[0])
                dy1 = (a1[1] - a2[1])
                dx2 = (a1[0] - i)
                dy2 = (a1[1] - j)
                sl1 = inf if dx1 == 0 else dy1/dx1
                sl2 = inf if dx2 == 0 else dy2/dx2
                if sl1 == sl2:
                    if (i, j) == (2, 0): print(k, l, a1, a2, sl1, sl2)
                    s += 1
                    br = True
                    break
            if br: break
print(s)