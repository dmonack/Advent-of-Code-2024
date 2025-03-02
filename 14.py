# Advent of Code 2024 - Day 14

robots = []
with open('data14.txt', 'r') as f:
    for line in f.readlines():
        p, v = line.split()
        px, py = p.split(',')
        vx, vy = v.split(',')
        robots.append((int(px[2:]), int(py), int(vx[2:]), int(vy)))
    
height, width, time = 103, 101, 100
quads = [0, 0, 0, 0, 0] # border, upper right, upper left, lower left, lower right
time = 100

def quadrant(x, y)->int:
    mid_x = width // 2
    mid_y = height // 2
    
    if x == mid_x or y == mid_y:
        return 0
    
    right, bottom = x > mid_x, y > mid_y
    
    if right and not bottom:
        return 1
    
    if not right and not bottom:
        return 2
    
    if not right and bottom:
        return 3
    
    if right and bottom:
        return 4
    
    raise ValueError("Can't find quadrant")

for px, py, vx, vy in robots:
    x = (px + vx * time) % width
    y = (py + vy * time) % height
    quads[quadrant(x, y)] += 1
    
print(quads)
ans1 = quads[1] * quads[2] * quads[3] * quads[4]
    
print(f"Part 1 answer: {ans1}")
# 217132650 is correct

def display(t: int):
    screen = []
    for _ in range(height):
        screen.append(['.'] * width)
        
    for px, py, vx, vy in robots:
        screen[(py + vy * t) % height][(px + vx * t) % width] = 'X'
        
    for row in screen:
        print(''.join(row))
        
    print("Time:", t)

# Part 2
t = 0
while True:
    positions = set()
    score = 0
        
    for px, py, vx, vy in robots:
        positions.add( ((py + vy * t) % height, (px + vx * t) % width) )

    for x, y in positions:
        if (x+1, y) in positions or (x-1, y) in positions:
            score += 1
            
    if score > 150:
        display(t)
        break
    
    t += 1

# 6516 is correct