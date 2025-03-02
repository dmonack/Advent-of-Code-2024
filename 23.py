# Advent of Code 2024 - Day 23

from collections import defaultdict
from itertools import combinations as combos

test = False

connections = defaultdict(list)

if test:
    loc = 'test23.txt'
else:
    loc = 'data23.txt'

with open(loc, 'r') as f:
    for line in f.readlines():
        a, b = line.strip().split('-')
        if a.startswith('t'):
            a = '~' + a[1:]
        if b.startswith('t'):
            b = '~' + b[1:]

        if a < b:
            connections[a].append(b)
        else:
            connections[b].append(a)

nodes = list(connections.keys())
nodes.sort()
for node in nodes:
    print(node, connections[node])

# print(connections)

# Part 1
count: int = 0
for a, v in connections.items():
    nodelist = sorted(v)
    for i, b in enumerate(nodelist):
        if b in connections:
            for c in nodelist[i+1:]:
                if c in connections[b]:
                    # print(a, b, c)
                    if c.startswith('~'):
                        # print('***')
                        count += 1

print(f'Part 1 answer: {count}')
# 1170 is correct

# Part 2
def is_clique(nodes: list[str]) -> bool:
    nodes.sort()
    for i, a in enumerate(nodes):
        for b in nodes[i+1:]:
            if b not in connections[a]:
                return False
    return True

max_clique = []
clique_size = 0
for node in nodes:
    n = len(connections[node]) + 1
    while n > clique_size:
        for combo in combos(connections[node], n - 1):
            if is_clique([node] + list(combo)):
                max_clique = [node] + list(combo)
                clique_size = n
                break
        n -= 1

max_clique.sort()
print(f'Part 2 answer: {','.join(max_clique)}  size: {clique_size}')
# correct: bo,dd,eq,ik,lo,lu,ph,ro,rr,rw,uo,wx,yg, size: 13
    