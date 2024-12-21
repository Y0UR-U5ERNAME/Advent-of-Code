with open('input9.txt') as f:
    d = list(map(int, f.read().strip()))

s = 0
b = []
I = 0
j = len(d) - 2 if len(d) % 2 == 0 else len(d) - 1
for i in range(0, len(d), 2):
    if i > j: break
    s += sum(i // 2 * (I + k) for k in range(d[i]))
    I += d[i]

    while len(b) < d[i+1]:
        if j <= i: break
        b += [j // 2 for k in range(d[j])]
        j -= 2
    s += sum(b[k] * (I + k) for k in range(len(b) if i == j else min(len(b), d[i + 1])))
    b = b[d[i+1]:]
    I += d[i + 1]
print(s)

s = 0
I = 0
used = []
free = []
for i in range(0, len(d), 2):
    used.append((I, d[i], i // 2))
    I += d[i]
    if i + 1 < len(d) and d[i + 1]:
        free.append((I, d[i + 1]))
        I += d[i + 1]
print(used)
print(free)
for i in range(len(used) - 1, -1, -1):
    for j in range(len(free)):
        if free[j][1] >= used[i][1] and free[j][0] < used[i][0]:
            used[i], free[j] = (free[j][0], used[i][1], used[i][2]), (free[j][0] + used[i][1], free[j][1] - used[i][1])
            break
    free = [j for j in free if j[1]]
print(used)
print(free)
for i in used:
    s += i[2] * sum(i[0] + j for j in range(i[1]))
print(s)