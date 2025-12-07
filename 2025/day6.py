with open('input6.txt') as f:
    count = 0
    count2 = 0
    inp = []
    d = f.read().split('\n')
    for i in d: inp.append(i.split())
    inp = [[inp[j][i] for j in range(len(inp))] for i in range(len(inp[0]))]
    inp2 = []
    toadd = []
    for i in range(len(d[0])):
        toaddtoadd = ''.join(d[j][-1-i] for j in range(len(d)))
        if not toaddtoadd.strip(): continue
        if toaddtoadd.endswith('+') or toaddtoadd.endswith('*'):
            toadd += [toaddtoadd[:-1], toaddtoadd[-1]]
            inp2.append(toadd)
            toadd = []
        else: toadd.append(toaddtoadd)
    for k in 0, 1:
        for i in (inp2 if k else inp):
            op = i[-1]
            out = 0 if op == '+' else 1
            for j in i[:-1]:
                if op == '+': out += int(j)
                else: out *= int(j)
            if k: count2 += out
            else: count += out

print(count)
print(count2)