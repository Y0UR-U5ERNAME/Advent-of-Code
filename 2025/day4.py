with open('input4.txt') as f:
    count = 0
    count2 = 0
    map = []
    neighbors = []
    for i in f.read().split('\n'):
        map.append(list(i))
        neighbors.append([0 for _ in range(len(i))])
    torem = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != '@': continue
            c = 0
            for k, l in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                x, y = i + k, j + l
                if not (0 <= x < len(map) and 0 <= y < len(map[0])): continue
                if map[x][y] == '@': c += 1
            neighbors[i][j] = c
            if c < 4:
                torem.add((i, j))
                count += 1
    while torem:
        nexttorem = set()
        for i, j in torem:
            count2 += 1
            map[i][j] = '.'
            neighbors[i][j] = 0
            for k, l in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                x, y = i + k, j + l
                if not (0 <= x < len(map) and 0 <= y < len(map[0])) or (x, y) in torem: continue
                if map[x][y] == '@':
                    neighbors[x][y] -= 1
                    if neighbors[x][y] < 4: nexttorem.add((x, y))
        torem = nexttorem

print(count)
print(count2)