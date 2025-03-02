from collections import Counter

# part 1
diff: int = 0
a, b = [], []

with open("data01.txt") as f:
    for line in f.readlines():
        left, right, *_ = line.split()
        a.append(int(left))
        b.append(int(right))

a.sort()
b.sort()

for left, right in zip(a, b):
    diff += abs(left - right)

print(f"Part 1 Answer: {diff}")

# 30556239 too high
# 2264607 correct

# Part 2
count = Counter(b)
similarity = 0

for val in a:
    similarity += val * count[val]

print(f"Part 2 answer: {similarity}")

# 19457120 correct