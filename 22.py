# Advent of Code 2024 - Day 22

from collections import defaultdict

test = False
if test:
    numbers = [1, 2, 3, 2024]
else:
    with open('data22.txt', 'r') as f:
        numbers = []
        for line in f.readlines():
            numbers.append(int(line))

# 64 = 2 ** 6
# 32 = 2 ** 5
# 2048 = 2 ** 11
# 16777216 = 2 ** 24

def secret(n):
    a = n << 6  # n = n * 64
    n ^= a
    n %= 16777216 # 2 ** 24 (Use only last 24 bits)
    b = n >> 5
    n ^= b
    n = n % 16777216
    c = n << 11
    n ^= c
    return n % 16777216

def repeated(n, q):
    for _ in range(q):
        n = secret(n)

    return n

ans1 = sum(map(lambda x: repeated(x, 2000), numbers))

print(f'Part1 answer is {ans1}')
# 13461553007 is correct

# Part 2
def locate(vals: list[int, int, int, int, int])->tuple[int, int, int, int]:
    ret = (vals[i]-vals[i-1] for i in range(1, 5))
    return tuple(ret)

prices = defaultdict(int)
ans2 = 0

for seed in numbers:
    seen = set()
    curr = seed
    vals = []

    for _ in range(2000):
        vals.append(curr % 10)
        curr = secret(curr)
        if len(vals) < 5:
            continue
        diffs = locate(vals[-5:])
        if diffs not in seen:
            seen.add(diffs)
            prices[diffs] += vals[-1]
            ans2 = max(ans2, prices[diffs])

    # print(vals)

# print(prices, seen)
# print(f'Part2 answer is {ans2}')
# 2816627541 is too high
# 1499 is correct!