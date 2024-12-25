with open('input24.txt') as f:
    l = f.read().strip().split('\n')
idx = l.index('')
l1 = {i.split(': ')[0]: int(i.split(': ')[1]) for i in l[:idx]}
l2 = {i.split(' ')[4]: i.split(' ')[:3] for i in l[idx+1:]}

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b
}

def rec(i):
    if i in l1: return l1[i]
    return ops[l2[i][1]](rec(l2[i][0]), rec(l2[i][2]))

s = 0
for i in l2:
    if i[0] == 'z':
        s += rec(i) << int(i[1:])
print(s)

def rec2(i):
    if i in l1: return l1[i]
    out = ops[l2[i][1]](rec2(l2[i][0]), rec2(l2[i][2]))
    print(i, l2[i], out)
    return out

# manually look for gates to swap based on wrong bits
for I in range(45):
    i = 1 << I
    for j in l1:
        l1[j] = (i >> int(j[1:])) & 1
    xn = sum(l1[i] << int(i[1:]) for i in l1 if i[0] == 'x')
    yn = sum(l1[i] << int(i[1:]) for i in l1 if i[0] == 'y')
    zn = {i: ((xn + yn) >> i) & 1 for i in range(len(l1) // 2 + 1)}
    rz = {i: rec('z' + str(i).rjust(2, '0'))  for i in range(len(l1) // 2 + 1)}
    wrong = [i for i in zn if zn[i] != rz[i]]
    if wrong:
        rec2('z' + str(wrong[0]).rjust(2, '0'))
        print(zn[wrong[0]], rz[wrong[0]])
        print(i, wrong)

'''
  ABC
+ DEF
-----
 GHIJ

J = C ^ F
I = B ^ E ^ (C & F)
H = A ^ D ^ ...
...
'''