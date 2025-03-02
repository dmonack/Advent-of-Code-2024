# Advent of Code 2024 - Day 11

from collections import defaultdict

# data, steps = [125, 17], 25 # test data
data, steps = [4189, 413, 82070, 61, 655813, 7478611, 0, 8], 75

hmap = {x: 1 for x in data}

def transform(n: int)->list:
    if n == 0:
        return [1]
    
    if len(word := str(n)) % 2 == 0:
        half = len(word) // 2
        left, right = int(word[:half]), int(word[half:])
        return [left, right]

    return [n * 2024]


# Part 1
# 186203 is correct

ans = 0

# Part 2
for _ in range(steps):
    nextd = defaultdict(int)
    for n, v in hmap.items():
        for val in transform(n):
            nextd[val] += v

    hmap = nextd
print(hmap)    

ans = sum(hmap.values())

print(f'Part 2 answer is {ans}')
# 221291560078593 is correct