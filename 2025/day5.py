with open('input5.txt') as f:
    count = 0
    count2 = 0
    isrange = True
    ranges = set()
    for i in f.read().split('\n'):
        if not i: isrange = False; continue
        if isrange:
            lo, hi = map(int, i.split('-'))
            for j, k in ranges.copy():
                if j <= lo <= k or j <= hi <= k or lo <= j <= k <= hi:
                    lo, hi = min(j, lo), max(k, hi)
                    ranges.remove((j, k))                    
            ranges.add((lo, hi))
        else: count += any(j <= int(i) < k for j, k in ranges)
    for i, j in ranges: count2 += j - i + 1

print(count)
print(count2)