import itertools
from math import ceil, log

with open('input7.txt') as f:
    d = [[int(i.split()[0][:-1]), list(map(int, i.split()[1:]))] for i in f.readlines()]

s = 0
for i in d:
    test, nums = i
    p = list(itertools.product([0, 1], repeat=len(nums) - 1))
    for j in p:
        n = nums[0]
        idx = 0
        for k in j:
            m = nums[idx + 1]
            if k == 0: n += m
            else: n *= m
            idx += 1
        if n == test:
            s += test
            break
print(s)

s = 0
for i in d:
    test, nums = i
    p = list(itertools.product([0, 1, 2], repeat=len(nums) - 1))
    for j in p:
        n = nums[0]
        idx = 0
        for k in j:
            m = nums[idx + 1]
            if k == 0: n += m
            elif k == 1: n *= m
            else: n = n * 10**ceil(log(m, 10)) + m
            idx += 1
        if n == test:
            s += test
            break
print(s)