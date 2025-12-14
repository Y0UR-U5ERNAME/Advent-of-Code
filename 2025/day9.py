with open('input9.txt') as f:
    count = 0
    count2 = 0
    reds = [tuple(map(int, i.split(','))) for i in f.read().split('\n')]
    rects = sorted((((i:=reds[I]), (j:=reds[J]), (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)) for I in range(len(reds)) for J in range(I + 1, len(reds))), key=lambda x: x[2], reverse=True)
    count = rects[0][2]
    for i, j, area in rects:
        minx, maxx = min(i[0], j[0]), max(i[0], j[0])
        miny, maxy = min(i[1], j[1]), max(i[1], j[1])
        if any(not (k[0] in (minx, maxx) and k[1] in (miny, maxy)) and minx <= k[0] <= maxx and miny <= k[1] <= maxy for k in reds): continue
        if any((minx < k[0] < maxx and k[1] < miny < l[1] if (k:=reds[K])[0] == (l:=reds[(K+1)%len(reds)])[0] else miny < k[1] < maxy and k[0] < minx < l[0]) for K in range(len(reds))): continue
        count2 = area
        break

print(count)
print(count2)