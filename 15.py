# Advent of Code 2024 - Day 15

from collections import deque


mapp, mapp2 = [], []
instructions: str = ''
convert = {'#': ['#', '#'], '.': ['.','.'], 'O': ['S', 'Z'], '@': ['@', '.']}

with open('data15.txt', 'r') as f:
    for row, line in enumerate(f.readlines()):
        if line[0] == '#':
            line2 = []
            mapp.append(list(line))
            for x in line.rstrip():
                line2.extend(convert[x])
                
            mapp2.append(line2)
            
            if '@' in line:
                bot_y, bot_x = row, line.index('@')
                bot2_y, bot2_x = row, line2.index('@')
            
        else:
            instructions += line
            
for line in mapp2:
    print(''.join(line))
    
box_value = lambda y, x: y * 100 + x

# make moves
dir = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1)}
for instr in instructions:
    if instr == '\n':
        continue
    delta_y, delta_x = dir[instr]
    y, x = bot_y, bot_x
    while mapp[y][x] not in ('#', '.'):
        y += delta_y
        x += delta_x
        
    if mapp[y][x] == '.':
        mapp[y][x] = 'O'
        mapp[bot_y][bot_x] = '.'
        bot_y += delta_y
        bot_x += delta_x
        mapp[bot_y][bot_x] = '@'
        
        
# make moves in mapp2
n = 0
for instr in instructions:
    if instr in ('>', 'v'):
        delta = 1
    elif instr in ('<', '^'):
        delta = -1
    else:
        delta = 0
    
    y, x = bot2_y, bot2_x

    if instr in ('<', '>'):  # straightforward x-axis movement
        while mapp2[y][x] != '#':
            if mapp2[y][x] == '.':
                # move stuff
                for loc in range(x, bot2_x, -delta):
                    mapp2[y][loc] = mapp2[y][loc - delta]
                mapp2[y][bot2_x] = '.'
                bot2_x += delta
                mapp2[y][bot2_x] = '@'
                break
            x += delta
            
    elif instr in ('^', 'v'):  # more complex vertical movement
        stack = []
        q = deque([(bot2_x, bot2_y)])
        move = True
        while q:
            x, y = q.popleft()
            if (beneath := mapp2[y + delta][x]) == '#':  # no movement
                move = False
                break
            elif beneath == 'S':
                if (x, y+delta) not in q:
                    q.append((x, y+delta))
                if (x+1, y+delta) not in q:                         
                    q.append((x+1, y+delta))
            elif beneath == 'Z':
                if (x, y+delta) not in q:
                    q.append((x, y+delta))
                if (x-1, y+delta) not in q:                         
                    q.append((x-1, y+delta))
                    
            stack.append((x, y))

        if move:
            for x, y in stack[::-1]:
                mapp2[y + delta][x] = mapp2[y][x]
                mapp2[y][x] = '.'
                    
            bot2_y += delta

    # print(instructions)

    """     if (response := input('Go on?')) == 'q':
        exit() """
        
"""     n += 1
    if True:
        if instr == '\n':
            n -= 1
            continue
        print(n, instr)
        for line in mapp2:
            print(''.join(line)) """
    
# evaluate
ans1 = 0
for y, row in enumerate(mapp):
    for x, c in enumerate(row):
        if c == 'O':
            ans1 += box_value(y, x)
            
            
print(f'Part 1 answer is {ans1}')
# 1406628 is correct

ans2 = 0
for y, row in enumerate(mapp2):
    for x, c in enumerate(row):
        if c == 'S':
            ans2 += box_value(y, x)
            
print(f'Part 2 answer is {ans2}')
# 1015927 is too low
# 1432781 is right!