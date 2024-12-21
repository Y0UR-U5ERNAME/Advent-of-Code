with open('input21.txt') as f:
    l = f.read().strip().split('\n')

numpos = {
    '0': (1, 3),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    'A': (2, 3)
}

dirpos = {
    '^': (1, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
    'A': (2, 0)
}

from itertools import product
from functools import lru_cache

def numpathsto(x, y, tox, toy):
    h = '>' * (tox - x) if x < tox else '<' * (x - tox)
    v = 'v' * (toy - y) if y < toy else '^' * (y - toy)
    if x == 0 and toy == 3: return {h + v + 'A'}
    if y == 3 and tox == 0: return {v + h + 'A'}
    return {h + v + 'A', v + h + 'A'}

def dirpathsto(x, y, tox, toy):
    h = '>' * (tox - x) if x < tox else '<' * (x - tox)
    v = 'v' * (toy - y) if y < toy else '^' * (y - toy)
    if x == 0 and toy == 0: return h + v + 'A'
    if y == 0 and tox == 0: return v + h + 'A'
    # https://www.reddit.com/r/adventofcode/comments/1hjgyps/2024_day_21_part_2_i_got_greedyish/
    # horizontal first if going left, otherwise vertical first
    if h == '<': return h + v + 'A'
    return v + h + 'A'

def num2dir(num):
    out = []
    x, y = 2, 3
    for i in num:
        tox, toy = numpos[i]
        out.append(numpathsto(x, y, tox, toy))
        x, y = tox, toy
    return [''.join(i) for i in product(*out)]

def dir2dir(dir, x=2, y=0):
    out = []
    for i in dir:
        tox, toy = dirpos[i]
        out.append(dirpathsto(x, y, tox, toy))
        x, y = tox, toy
    return [''.join(out), x, y]

@lru_cache(maxsize=10000)
def r(i, depth):
    if depth == 0: return len(i)
    out = 0
    x, y = 2, 0
    for j in i:
        G = dir2dir(j, x, y)
        out += r(G[0], depth - 1)
        x, y = G[1:]
    return out

for n in (2, 25):
    s = 0
    for i in l:
        a = [r(j, n) for j in num2dir(i)]
        print(min(a))
        s += min(a) * int(i[:-1])
    print(s)