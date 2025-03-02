# Advent of Code 2024 - Day 8
from collections import defaultdict
from itertools import permutations as pe

with open("data08.txt") as f:
    mapp = f.readlines()
    
mapp = [line.rstrip() for line in mapp]
nodes = defaultdict(list)
antinodes = set()
antinodes2 = set()

height, width = len(mapp), len(mapp[0])
inrange = lambda y, x: (0 <= y < height) and (0 <= x < width)

for y in range(height):
    for x in range(width):
        c = mapp[y][x]
        if c != '.':
            nodes[c].append((y, x))
            
for c in nodes.keys():
    for a, b in pe(nodes[c], 2):
        delta_y, delta_x = b[0]-a[0], b[1]-a[1]
        anti1 = (b[0] + delta_y, b[1] + delta_x)
        anti2 = (a[0] - delta_y, a[1] - delta_x)
        if inrange(*anti1):
            antinodes.add(anti1)
            
        if inrange(*anti2):
            antinodes.add(anti2)
            
        # for part 2:
        y, x = b
        while inrange(y, x):
            antinodes2.add((y, x))
            y += delta_y
            x += delta_x
            
        y, x = a
        while inrange(y, x):
            antinodes2.add((y, x))
            y -= delta_y
            x -= delta_x
                    
print(antinodes2)

print(f'Part 1 answer is {len(antinodes)}')
# 367 is correct!

print(f'Part 2 answer: {len(antinodes2)}')
# 1285 is correct!

