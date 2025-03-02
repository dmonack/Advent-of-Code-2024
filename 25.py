# Advent of Code 2024 - Day 25

test = True

if test:
    filename = 'data25.txt'
else:
    filename = 'test25.txt'


keys: list[list[int]] = []
locks: list[list[int]] = []

with open(filename) as f:
    lines = f.readlines()

for i in range(0, len(lines), 8):
    if lines[i].startswith('#'): # lock
        locks.append([0,0,0,0,0])
        item = locks[-1]
    else: # key
        keys.append([0,0,0,0,0])
        item = keys[-1]

    for line in lines[i+1:i+6]:
        for j, c in enumerate(line.strip()):
            if c == '#':
                item[j] += 1
    
def fit(key: list[int], lock: list[int]) -> bool:
    for i in range(5):
        if key[i] > 5 - lock[i]:
            return False
    return True
    
ans1 = 0
for key in keys:
    for lock in locks:
        if fit(key, lock):
            ans1 += 1

print(f'Part 1 answer: {ans1}')
# 3525 is correct