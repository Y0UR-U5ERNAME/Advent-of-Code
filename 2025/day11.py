from functools import cache

@cache
def pathsfrom(a, b):
    if a == b: return 1
    out = 0
    if a in conns:
        for i in conns[a]: out += pathsfrom(i, b)
    return out

with open('input11.txt') as f:
    conns = {}
    for i in f.read().split('\n'): l = i.split(' '); conns[l[0][:-1]] = l[1:]
    count = pathsfrom("you", "out")
    count2 = pathsfrom("svr", "dac") * pathsfrom("dac", "fft") * pathsfrom("fft", "out") + pathsfrom("svr", "fft") * pathsfrom("fft", "dac") * pathsfrom("dac", "out")

print(count)
print(count2)