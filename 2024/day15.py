with open('input15.txt') as f:
    l = f.read().split('\n')
n = l.index('')
m = [list(i) for i in l[:n]]
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
d = [dirs['v<^>'.index(i)] for i in ''.join(l[n+1:])]

xy = next((i, j) for i in range(len(m[0])) for j in range(len(m)) if m[j][i] == '@')

for D in d:
    nx = xy[0] + D[0]
    ny = xy[1] + D[1]
    txy = xy
    ok = False
    while m[txy[1]][txy[0]] != '#':
        txy = (txy[0] + D[0], txy[1] + D[1])
        if m[txy[1]][txy[0]] == '.':
            ok = True
            break
    if ok:
        m[xy[1]][xy[0]] = '.'
        xy = (nx, ny)
        m[txy[1]][txy[0]] = 'O'
        m[ny][nx] = '@'
print(sum(c * 100 + d for c, i in enumerate(m) for d, j in enumerate(i) if j == 'O'))

m = [list(''.join(k*2 for k in i).replace('@@', '@.').replace('OO', '[]')) for i in l[:n]]
xy = next((i, j) for i in range(len(m[0])) for j in range(len(m)) if m[j][i] == '@')

def pushable(x, y, D, both=False):
    t = m[y][x]
    if t == '.': return True
    if t == '#': return False
    ok = True
    if D[0] == 0 and both:
        if t == '[':
            ok = pushable(x + 1, y, D, not both)
        elif t == ']':
            ok = pushable(x - 1, y, D, not both)
    return ok and pushable(x + D[0], y + D[1], D, True)

def push(x, y, D, new, both=False):
    t = m[y][x]
    if t == '.':
        m[y][x] = new
        #print(f'\033[36m\033[{y+2};{x+1}H{new}\033[0m')
        return
    if t == '#': return
    if D[0] == 0 and both:
        if t == '[':
            push(x + 1, y , D, '.', not both)
        elif t == ']':
            push(x - 1, y , D, '.', not both)
    push(x + D[0], y + D[1], D, t, True)
    m[y][x] = new
    #print(f'\033[36m\033[{y+2};{x+1}H{new}\033[0m')

#print('\n'.join(''.join(j).replace('.', '\033[30m.\033[0m').replace('[]', '\033[35m[]\033[0m') for j in m))
for D in d:
    nx = xy[0] + D[0]
    ny = xy[1] + D[1]
    if pushable(xy[0], xy[1], D, False):
        t = m[ny][nx]
        push(xy[0], xy[1], D, '.', False)
        xy = (nx, ny)
#print(f'\033[{len(m)+1};1H')
print(sum(c * 100 + d for c, i in enumerate(m) for d, j in enumerate(i) if j == '['))