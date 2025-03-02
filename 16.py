# Advent of Code 2024 - Day 16

from numpy import full, uint32

mapp = []
with open('data16.txt', 'r') as f:
    for line in f.readlines():
        if 'E' in line:
            goal_y, goal_x = len(mapp), line.index('E')
            
        if 'S' in line:
            start = (len(mapp), line.index('S'))
            
        mapp.append(line.rstrip())
        
height, width = len(mapp), len(mapp[0])
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 0: N, 1: W, 2: S, 3: E
q = [(*start, 3)] # begin facing east
vals = full((height, width, 4), 85_500, dtype=uint32) # col, row, direction
vals[start[0]][start[1]][3] = 0

# print('\n'.join(mapp))

n = 0
while q:
    n += 1
    y, x, facing = q.pop()
    forward = (y + directions[facing][0], x + directions[facing][1])
    left, right = (facing - 1) % 4, (facing + 1) % 4
    
    val = vals[y][x][facing]
    
    """ if n % 10000 == 0:        
        print(f'{n//1000}k: row: {y}, col: {x}, {'NWSE'[facing]}; {val=}') """
              
    # check forward
    if (mapp[forward[0]][forward[1]] in ('.', 'S', 'E') and
        vals[forward[0]][forward[1]][facing] > val + 1):
        vals[forward[0]][forward[1]][facing] = val + 1
        q.append((*forward, facing))
        
    for turn in (left, right):
        if val + 1000 < vals[y][x][turn]:
            vals[y][x][turn] = val + 1000
            q.append((y, x, turn))
            
ans1 = min(vals[goal_y][goal_x])
print(f'Part 1 answer is {ans1}')
# 85480 is correct!
    
# Part2
print(vals)
paths = [[(*start, 3)]]
tiles = set()

while paths:
    # print(paths)
    path = paths.pop()
    y, x, facing = path[-1][0], path[-1][1], path[-1][2]
    val = vals[y][x][facing]
    
    # print(f'{y}, {x}, {"NWSE"[facing]}, {val=}')
    
    if val > ans1:
        continue
    
    if y == goal_y and x == goal_x: # valid path
        tiles.update((a, b) for a, b, _ in path)
        print(path)
    
    elif facing in (0, 2): # vertical
        if val + 1000 == vals[y][x][1]:
            paths.append(path + [(y, x, 1)])
        if val + 1000 == vals[y][x][3]:
            paths.append(path + [(y, x, 3)])
            
    elif facing in (1, 3): # horizontal
        if val + 1000 == vals[y][x][0]:
            paths.append(path + [(y, x, 0)])
        if val + 1000 == vals[y][x][2]:
            paths.append(path + [(y, x, 2)]) 
            
    y += directions[facing][0]
    x += directions[facing][1]
    
    if val + 1 == vals[y][x][facing]:
        paths.append(path + [(y, x, facing)])
        
    # clsprint(f'No. of paths: {len(paths)}, No. of tiles: {len(tiles)}')
        
print(f'Part 2 answer is {len(tiles)}')
# 518 is correct!