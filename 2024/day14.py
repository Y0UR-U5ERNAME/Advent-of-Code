from time import sleep
from math import lcm
from copy import deepcopy

with open('input14.txt') as f:
    d = [[eval(i[2:i.index(' ')]), eval(i.strip()[i.index('v')+2:])] for i in f.readlines()]

w = 101
h = 103
q = [[0, 0], [0, 0]]
D = deepcopy(d)
for c, i in enumerate(D):
    D[c][0] = ((D[c][0][0] + D[c][1][0] * 100) % w, (D[c][0][1] + D[c][1][1] * 100) % h)
    if not(D[c][0][0] == w // 2 or D[c][0][1] == h // 2):
        q[D[c][0][0] < w // 2][D[c][0][1] < h // 2] += 1
print(q[0][0] * q[0][1] * q[1][0] * q[1][1])

'''
# manually find first christmas tree that appears
s = 0
o = 25 # first number where cluster appears
M = o
D = deepcopy(d)
n = 0
preq = float('inf')
while True:
    m = [['.' for k in range(w)] for j in range(h)]
    q = [[0, 0], [0, 0]]
    for c, i in enumerate(D):
        D[c][0] = ((D[c][0][0] + D[c][1][0] * M) % w, (D[c][0][1] + D[c][1][1] * M) % h)
        m[D[c][0][1]][D[c][0][0]] = '#'
        if not(D[c][0][0] == w // 2 or D[c][0][1] == h // 2):
            q[D[c][0][0] < w // 2][D[c][0][1] < h // 2] += 1
    s += M
    if s == o:
        #M = lcm(*[lcm(w, i[1][0] % w) // (i[1][0] % w) for i in D]) # vertical cluster
        M = lcm(*[lcm(h, i[1][1] % h) // (i[1][1] % h) for i in D]) # horizontal cluster
    Q = q[0][0] * q[0][1] * q[1][0] * q[1][1]
    if Q < preq:
        print(s)
        print('\n'.join([''.join(i) for i in m]))
        preq = Q
    sleep(.2)
    n += 1
'''

s = 0
D = deepcopy(d)
while len({tuple(i[0]) for i in D}) != len(D):
    for c, i in enumerate(D):
        D[c][0] = ((D[c][0][0] + D[c][1][0] * 1) % w, (D[c][0][1] + D[c][1][1] * 1) % h)
    s += 1
print(s)