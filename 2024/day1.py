with open('input1.txt') as f:
    l = [[int(j) for j in i.split()] for i in f.readlines()]
    l1 = sorted(i[0] for i in l)
    l2 = sorted(i[1] for i in l)
    print(sum(abs(i - j) for i, j in zip(l1, l2)))
    print(sum(i * l2.count(i) for i in l1))