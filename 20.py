# Advent of Code 2024 - Day 20

from numpy import full

test = False
if test:
    filename = "test20.txt"
    threshhold = 2
    
else:
    filename = "data20.txt"
    threshhold = 100

with open(filename, 'r') as f:
    mapp = [list(line) for line in f.readlines()]
    
height, width = len(mapp), len(mapp[0])
LARGE_N = 100_000_000
MAX_DISTANCE = 20

vals = full((height, width), LARGE_N, dtype=int)
# print(vals)

for y, row in enumerate(mapp):
    if 'S' in row:
        x = row.index('S')
        break
    
path = []
n = 0
while mapp[y][x] != 'E':
    vals[y][x] = n
    if n >= threshhold - 1:
        path.append((y, x))
    for a, b in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
        if mapp[a][b] != '#':
            mapp[y][x] = '#'
            y, x = a, b
            break
    n += 1
    
vals[y][x] = n
path.append((y, x))

# print(vals)
ans1 = 0
ans2 = 0

inside = lambda y, x: 0 <= y < height and 0 <= x < width and \
    vals[y][x] != LARGE_N

if test:
    test74 = 0
    
for y, x in path:
    val = vals[y][x]
    
    # Part 1
    for a, b in ((y, x + 2), (y, x - 2), (y + 2, x), (y - 2, x)):
        if inside(a, b):
            otherval = vals[a][b]
            if val - otherval - 2 >= threshhold:
                ans1 += 1
                # print(f'{y}, {x} <- {a}, {b}, saves: {val - otherval -2}')
                
    # Part 2
    for a in range(y - MAX_DISTANCE, y + MAX_DISTANCE + 1):
        max_horzontal = MAX_DISTANCE - abs(y - a)
        for b in range(x - max_horzontal, x + max_horzontal + 1):
            if inside(a, b):
                otherval = vals[a][b]
                if test and val - otherval + abs(a - y) + abs(b - x) == 74:
                    test74 += 1
                    print(f'{y}, {x} <- {a}, {b}')
                if val - otherval - abs(a - y) - abs(b - x) >= threshhold:
                    ans2 += 1
                
if test:
    print(f'Saving 74 picoseconds: {test74}')
    
print(f'Part 1 answer is {ans1}')
# 1331 is too high
# 1295 is too low
# 1307 is too high
# 1296 is correct
                
print(f'Part 2 answer is {ans2}')
# 83217 is too low
# 94671 is too low
# 1096591 is too high
# 977665 is correct