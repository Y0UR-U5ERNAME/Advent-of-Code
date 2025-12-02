with open('input2.txt') as f:
    count = 0
    count2 = 0
    for i in f.readline().split(','):
        low, high = map(int, i.split('-'))
        for j in range(low, high + 1):
            L = len(str(j))
            for l in range(L // 2, 0, -1):
                if L % l != 0: continue
                if j % sum(10 ** k for k in range(0, L, l)) == 0:
                    if L / 2 == l: count += j
                    count2 += j
                    break

print(count)
print(count2)