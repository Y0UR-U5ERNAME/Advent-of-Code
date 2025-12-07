with open('input7.txt') as f:
    count = 0
    count2 = 0
    map = f.read().split('\n')[::2]
    x = {map[0].index('S'): 1}
    for i in map:
        newx = x.copy()
        for j in x:
            if i[j] == '^':
                newx.pop(j)
                newx.setdefault(j - 1, 0)
                newx[j - 1] += x[j]
                newx.setdefault(j + 1, 0)
                newx[j + 1] += x[j]
                count += 1
        x = newx
    count2 = sum(x.values())

print(count)
print(count2)