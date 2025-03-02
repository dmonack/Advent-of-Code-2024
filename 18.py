# Advent of Code 2024 - Day 18

from collections import deque
from numpy import full

test = False

if test:
    width = 7
    file = 'test18.txt'
    bytes = 12

else:
    width = 71
    file = 'data18.txt'
    bytes = 1024

available: int = 0
mapp = full([width, width], available, dtype=int)
valid = lambda x, y: 0 <= x < width and 0 <= y < width

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines[:bytes]:
        x, y = line.split(',')
        mapp[int(y)][int(x)] = 1

# for part 2:
mapp2 = full([width, width], available, dtype=int)
blockers = []
for line in lines:
    if ',' in line:
        x, y = line.split(',')
        mapp2[int(y)][int(x)] = 1  # blocked
        blockers.append((int(x), int(y)))



# BFS
q = deque([(0, 0)])
ans1 = 0

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        if x == width -1 and y == width - 1:
            q = []
            print(f'Part 1 answer: {ans1}')
            # 232 is correct

            break
        if mapp[y][x] == available:
            mapp[y][x] = 1
            for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if valid(a, b):
                    q.append((a, b))

    ans1 += 1

# part 2
q = deque([(0,0)])
mapp2[0][0] = -1
# -1 = visited; 0 = open; 1 = blocked

while q:
    x, y = q.popleft()
    mapp2[y][x] = -1
    for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if valid(x,y) and mapp2[b][a] == available:
            q.append((a, b))

for x, y in blockers[::-1]:
    mapp2[y][x] = 0
    adjacents =  [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    if any(valid(x,y) and mapp2[y][x] == -1 for x, y in adjacents):
        q = deque([(x, y)])
        while q:
            a, b = q.popleft()
            mapp2[b][a] = -1
            if a == width - 1 and b == width - 1:
                print(f'Part 2 answer is ({x},{y})')
                # 44,64 is correct!
                break
            for c, d in [(a+1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                if valid(c, d) and mapp2[d][c] == 0:
                    q.append((c, d))


print("End of program.")
