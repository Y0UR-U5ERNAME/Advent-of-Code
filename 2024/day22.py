with open('input22.txt') as f:
    l = list(map(int, f.read().strip().split('\n')))

bananas = [[] for i in l]
s = 0
for c, i in enumerate(l):
    n = i
    for j in range(2000):
        i ^= i << 6
        i &= 16777216 - 1
        i ^= i >> 5
        i &= 16777216 - 1
        i ^= i << 11
        i &= 16777216 - 1
        bananas[c].append(i % 10)
    s += i
print(s)

changes = [[] for i in bananas]
for c, i in enumerate(bananas):
    for j in range(len(i)-1):
        changes[c].append(i[j+1] - i[j])

seq = {}
for c, j in enumerate(changes):
    seen = set()
    for k in range(len(j)-4+1):
        s = tuple(j[k:k+4])
        b = bananas[c][k+4]
        if s not in seen:
            if s not in seq: seq[s] = 0
            seq[s] += b
            seen.add(s)
print(max(seq.values()))