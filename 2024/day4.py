with open('input4.txt') as f:
    d = f.readlines()

w = len(d[0]) - 1
h = len(d)
print(w, h)
s = 0
for j in range(h):
    for i in range(w):
        l = []
        o = False
        if w - i >= 4:
            l.append(d[j][i:i+4])
        if h - j >= 4:
            l.append(''.join([k[i] for k in d[j:j+4]]))
            if w - i >= 4:
                l.append(d[j][i] + d[j+1][i+1] + d[j+2][i+2] + d[j+3][i+3])
            if i >= 3:
                l.append(d[j][i] + d[j+1][i-1] + d[j+2][i-2] + d[j+3][i-3])
        s += l.count('XMAS') + l.count('SAMX')
print(s)

s = 0
for j in range(h - 2):
    for i in range(w - 2):
        a = (d[j][i] + d[j+1][i+1] + d[j+2][i+2])
        b = (d[j+2][i] + d[j+1][i+1] + d[j][i+2])
        s += a in ('MAS', 'SAM') and b in ('MAS', 'SAM')
print(s)