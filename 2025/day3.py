with open('input3.txt') as f:
    count = 0
    count2 = 0
    for i in f.read().split('\n'):
        for b in 2, 12:
            maxsum = 0
            mxi = -1
            for N in range(b):
                mx = -1
                for c in range(mxi + 1, len(i) - (b - 1 - N)):
                    n = int(i[c])
                    if n > mx: mx = n; mxi = c
                maxsum = maxsum * 10 + mx
            if b == 2: count += maxsum
            else: count2 += maxsum

print(count)
print(count2)