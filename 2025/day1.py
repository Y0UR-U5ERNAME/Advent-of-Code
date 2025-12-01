with open('input1.txt') as f:
    count = 0
    count2 = 0
    r = 50
    for i in f.readlines():
        newr = r + (int(i[1:]) if i[0] == 'R' else -int(i[1:]))
        #count2 += abs(newr // 100) + (newr <= 0 and newr % 100 == 0 if r else -(newr < 0))
        count2 += abs((abs(newr - 50) + 50) // 100) - (r == 0 and newr < 0)
        r = newr % 100
        if r == 0: count += 1

print(count)
print(count2)