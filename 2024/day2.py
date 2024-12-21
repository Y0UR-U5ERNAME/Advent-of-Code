with open('input2.txt') as f:
    l = [[int(j) for j in i.split()] for i in f.readlines()]
    
print(sum((i == sorted(i) or i == sorted(i)[::-1]) and all(1 <= abs(i[j+1]-i[j]) <= 3 for j in range(len(i) - 1)) for i in l))
s = 0
for i in l:
    for k in range(len(i)):
        I = [j for c, j in enumerate(i) if c != k]
        if (I == sorted(I) or I == sorted(I)[::-1]) and all(1 <= abs(I[j+1]-I[j]) <= 3 for j in range(len(I) - 1)):
            s += 1
            break
print(s)