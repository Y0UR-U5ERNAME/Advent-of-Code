with open('input25.txt') as f:
    l = f.read().strip().split('\n')

locks = set()
keys = set()
for i in range(0, len(l), 8):
    heights = tuple([sum(k[j] == '#' for k in l[i:i+7]) for j in range(5)])
    if l[i] == '.....': keys.add(heights)
    else: locks.add(heights)

s = 0
for i in locks:
    for j in keys:
        if all([i[k] + j[k] <= 7 for k in range(5)]):
            s += 1
print(s)