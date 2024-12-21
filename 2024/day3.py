with open('input3.txt') as f:
    d = f.read()

c = -4
s = 0
while c < len(d):
    c = d.find('mul(', c + 4)
    if c == -1: break
    if d[c:c+4] == 'mul(':
        e = d.find(',', c + 4)
        f = d.find(')', e + 1)
        try: s += int(d[c+4:e]) * int(d[e+1:f])
        except: pass
print(s)

c = 0
s = 0
go = True
while c < len(d):
    if d[c:c+4] == 'mul(' and go:
        e = d.find(',', c + 4)
        f = d.find(')', e + 1)
        try: s += int(d[c+4:e]) * int(d[e+1:f])
        except: pass
    elif d[c:c+4] == 'do()':
        go = True
    elif d[c:c+7] == "don't()":
        go = False
    c += 1
print(s)