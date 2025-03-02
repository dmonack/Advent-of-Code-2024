# Advent of Code 2024 - Day 6

with open("data06.txt") as f:
    mapp = [list(line.rstrip()) for line in f.readlines()]
    
for i, line in enumerate(mapp):
    if '^' in line:
        start_y, start_x = i, line.index('^')
        
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1)) # delta y, delta x
height, width = len(mapp), len(mapp[0])
in_range = lambda y, x: 0 <= y < height and 0 <= x < width
    
def vectors(y: int = start_y, x: int = start_x, dir: int = 0):
    while True:
        y += DIRECTIONS[dir][0]
        x += DIRECTIONS[dir][1]
        
        if not in_range(y, x):
            break
        
        if mapp[y][x] == '#': # backup and turn
            y -= DIRECTIONS[dir][0]
            x -= DIRECTIONS[dir][1]                
            dir = (dir + 1) % 4
            continue

        yield y, x, dir
        
path = list(vectors())
print(path)
points = {(a[0], a[1]) for a in path}
points.add((start_y, start_x))
print(points)

print(f"Part 1 answer: {len(points)}")
# 5305 is correct

# PART 2
blockers = 0
path_set = set()
for y, x, _ in path:
    path_set.add((y, x))
    
for y, x in path_set:
    # print(f"************* block at {y}, {x} *******************")
    prev_dir = 0
    seen = set()
    mapp[y][x] = '#'
    for vect in vectors():
        if vect[2] != prev_dir:
            prev_dir = vect[2]
            if vect in seen:
                blockers += 1
                # print(f"Loop at {vect}")
                break
            else:
                seen.add(vect)
    mapp[y][x] = '.'
#    print(f"Exit at {vect}")

print(f"Part 2 answer: {blockers}")
# 2402 is too high
# 662 is too low
# 2270 is too high
# 2269 is wrong
# 2143 is correct