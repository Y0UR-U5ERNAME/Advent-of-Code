with open('input7.txt') as f:
    count = 0
    count2 = 0
    map = f.read().split('\n')[::2]
    x = {map[0].index('S'): 1}
    for i in map:
        newx = {}
        for j in x:
            if i[j] == '^':
                newx.setdefault(j - 1, 0)
                newx[j - 1] += x[j]
                newx.setdefault(j + 1, 0)
                newx[j + 1] += x[j]
                count += 1
            else:
                newx.setdefault(j, 0)
                newx[j] += x[j]
        x = newx
    count2 = sum(x.values())

print(count)
print(count2)

'''
# array based 
with open('input7.txt') as f:
    count = 0
    count2 = 0
    map = f.read().split('\n')
    x = [int(i == 'S') for i in map[0]]
    for i in map:
        newcenter = 0
        for j in range(len(x)):
            xj = x[j]
            if xj and i[j] == '^':
                x[j] = newcenter
                x[j - 1] += xj
                newcenter = xj
                count += 1
            else:
                x[j] += newcenter
                newcenter = 0
    count2 = sum(x)

print(count)
print(count2)
'''