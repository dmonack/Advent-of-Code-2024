# Advent of Code 2024 - Day 10

part2 = True

testdata = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''

mapp = []

test = False
if test:
    for line in testdata.rstrip().split():
        mapp.append([int(x) for x in line.rstrip()])

else:
    with open("data10.txt") as f:
        for line in f.readlines():
            mapp.append([int(x) for x in line.rstrip()])
    
height, width = len(mapp), len(mapp[0])

def inside(coords: tuple[int, int])->bool:
    return 0 <= coords[0] < height and 0 <= coords[1] < width

def getval(coords: tuple[int, int])->int:
    y, x = coords
    if not inside(coords):
        raise ValueError(f"{y}, {x} outside bounds")
    
    return mapp[y][x]

starts = []
for y in range(height):
    for x in range(width):
        if mapp[y][x] == 0:
            starts.append((y, x))
            
ans = 0
for start_y, start_x in starts:
    val = 0
    q = [(start_y, start_x)]
    while q and val < 9:
        val += 1
        for _ in range(len(q)):
            y, x = q.pop(0)
            for point in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
                if (part2 or point not in q) and inside(point) and getval(point) == val:
                    q.append(point)
    ans += len(q)
    print(f'{start_y}, {start_x}: {q}')

print(f'{('Part 1', 'Part 2')[part2]} answer is {ans}')
# 1929 is too high
# 1120 is too high
# 496 is correct

# last wrong answer is the answer for part 2: 1120