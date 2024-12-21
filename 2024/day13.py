with open('input13.txt') as f:
    d = [(int(i[i.index('X')+2:i.index(',')]), int(i[i.index('Y')+2:])) for i in f.readlines() if i.strip()]
d = [d[i*3:i*3+3] for i in range(len(d) // 3)]

s = 0
for i in d:
    j = (i[2][1] * i[1][0] - i[1][1] * i[2][0]) / (i[0][1] * i[1][0] - i[1][1] * i[0][0])
    k = (i[2][0] - i[0][0] * j) / i[1][0]
    if j % 1 == 0 and k % 1 == 0: s += round(j)*3 + round(k)*1
print(s)

s = 0
for i in d:
    i[2] = (i[2][0] + 10000000000000, i[2][1] + 10000000000000)
    j = (i[2][1] * i[1][0] - i[1][1] * i[2][0]) / (i[0][1] * i[1][0] - i[1][1] * i[0][0])
    k = (i[2][0] - i[0][0] * j) / i[1][0]
    if j % 1 == 0 and k % 1 == 0: s += round(j)*3 + round(k)*1
print(s)