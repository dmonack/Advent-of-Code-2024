# Advent of Code 2024 - Day 12

from collections import defaultdict

with open('data12.txt', 'r') as f:
    grid = f.readlines()
    
ans1, ans2 = 0, 0

sections = defaultdict(lambda: [0, 0])

height, width = len(grid), len(grid[0])-1  # shorter width to remove endlines

inside = lambda y, x: 0 <= y < height and 0 <= x < width

def neighbors(y: int, x: int)->list[(int, int)]:
    return ((y+1, x), (y-1, x), (y, x+1), (y, x-1)) 

def count_corners(y: int, x: int)->int:
    base = grid[y][x]
    
    # neighbors starting at upper left
    neighbors = [(y-1, x-1), (y-1, x), (y-1, x+1),
                 (y, x+1), (y+1, x+1), (y+1, x),
                 (y+1, x-1), (y, x-1)]
    
    corners = [(7, 0, 1), (1, 2, 3), (3, 4, 5), (5, 6, 7)]

    neighbor_vals = []
    for a, b in neighbors:
        if not inside(a, b) or (grid[a][b] != base):
            neighbor_vals.append(False)
        else:
            neighbor_vals.append(True)
    
    count = 0
    for d, e, f in corners:
        a, b, c = neighbor_vals[d], neighbor_vals[e], neighbor_vals[f]
        if (a and c and not b) or not (a or c):
            count += 1
            
    return count

# failed method
""" for y in range(height):
    for x, region in enumerate(grid[y]):
        sections[region][0] += 1
        sections[region][1] += 4 - neighbors(y, x).count(region) """
        
seen = set()
for y in range(height):
    for x in range(width):
        if (y, x) not in seen:
            q = [(y, x)]
            name = grid[y][x]
            area, perimeter, corners = 0, 0, 0
            while q:
                curr = q.pop()
                if curr not in seen:
                    area += 1
                    corners += count_corners(*curr)
                    for a, b in neighbors(*curr):
                        if not inside(a,b) or grid[a][b] != name:
                            perimeter += 1    
                        else:
                            q.append((a, b))
                        
                    seen.add(curr)
                    
            print(f"{name}: {area=} {perimeter=} {corners=}")
            ans1 += area * perimeter
            ans2 += area * corners

print(f'Part 1 answer: {ans1}')
# 52333042 is too high
# 52294122 is too high
# 1396298 is correct

print(f'Part 2 answer: {ans2}')
# 2020782 is too high
# 844741 is too low
# 853588 is correct