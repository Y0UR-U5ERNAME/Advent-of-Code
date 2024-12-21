with open('input17.txt') as f:
    l = f.read().split('\n')
N = len('Register A: ')
a = int(l[0][N:])
b = int(l[1][N:])
c = int(l[2][N:])
d = list(map(int, l[4][9:].split(',')))

com = lambda x: (0, 1, 2, 3, a, b, c)[x]
ip = 0
s = []
while ip < len(d):
    opr = d[ip]
    opd = d[ip + 1]
    copd = com(opd)
    match opr:
        case 0: a >>= copd
        case 1: b ^= opd
        case 2: b = copd & 0b111
        case 3:
            if a: ip = opd; continue
        case 4: b ^= c
        case 5: s.append(copd & 0b111)
        case 6: b = a >> copd
        case 7: c = a >> copd
    ip += 2
print(','.join(map(str, s)))

outs = [set() for i in range(8)]
SHIFT = 3 # shift of A for every iteration
BITS = 10 # bits of A that are used in each iteration
SHIFTMASK = (1 << SHIFT) - 1
BITSMASK = (1 << BITS) - 1
for n in range(1 << BITS):
    a, b, c = n, 0, 0
    ip = 0
    while ip < len(d):
        opr = d[ip]
        opd = d[ip + 1]
        copd = com(opd)
        match opr:
            case 0: a >>= copd
            case 1: b ^= opd
            case 2: b = copd & 0b111
            case 3: pass
            case 4: b ^= c
            case 5:
                outs[copd & 0b111].add(n)
                break
            case 6: b = a >> copd
            case 7: c = a >> copd
        ip += 2

def r(idx, prev, full):
    if idx == len(d): return full
    n = d[idx]
    for i in outs[n]:
        if prev == None or prev >> SHIFT == i & ((1 << (BITS - SHIFT)) - 1):
            a = r(idx + 1, i, full | ((i & 0b111) << (idx * SHIFT)))
            if a != None: return a
print(r(0, None, 0))