from math import dist, prod

with open('input8.txt') as f:
    count = 0
    count2 = 0
    h = 0
    circs = {}
    boxes = {}
    for i in f.read().split('\n'): boxes[tuple(map(int, i.split(',')))] = -1
    lboxes = list(boxes.keys())
    dists = sorted([(lboxes[i], lboxes[j], dist(lboxes[i], lboxes[j])) for i in range(len(lboxes)) for j in range(i + 1, len(lboxes))], key=lambda x: x[2])
    c = 0
    for i, j, _ in dists:
        if not (-1 != boxes[i] == boxes[j]):
            if boxes[i] == -1:
                if boxes[j] == -1:
                    boxes[i] = h
                    boxes[j] = h
                    circs[h] = {i, j}
                    h += 1
                else:
                    boxes[i] = boxes[j]
                    circs[boxes[j]].add(i)
            else:
                if boxes[j] == -1:
                    boxes[j] = boxes[i]
                    circs[boxes[i]].add(j)
                else:
                    old = boxes[j]
                    for l in circs[boxes[j]]: boxes[l] = boxes[i]
                    circs[boxes[i]] |= circs[old]
                    circs.pop(old)
            if len(circs) == 1 and len(list(circs.values())[0]) == len(boxes): count2 = i[0] * j[0]; break
        c += 1
        if c == 1000: count = prod(sorted([len(i) for i in circs.values()], reverse=True)[:3])

print(count)
print(count2)