with open('input19.txt') as f:
    l = f.read().split('\n')

p = l[0].split(', ')
d = [i for i in l[2:] if i]

def f(des):
    if not len(des): return 1
    for i in p:
        if des.startswith(i) and f(des[len(i):]): return 1
    return 0

print(sum(f(i) for i in d))

from functools import lru_cache
@lru_cache(maxsize=10000)
def g(des):
    if not len(des): return 1
    out = 0
    for i in p:
        if des.startswith(i):
            out += g(des[len(i):])
    return out

print(sum(g(i) for i in d))