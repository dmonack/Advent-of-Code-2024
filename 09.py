# Advent of Code 2024 - Day 9

from collections import deque

test = False
part2 = True

with open("data09.txt") as f:
    files = f.read().rstrip()
    
sample = '2333133121414131402'

if test:
    files = sample

ans1: int = 0
size = len(files)
blocks = []
data = deque([i, int(x)] for i, x in enumerate(files[::2]))
empty = deque(int(x) for x in files[1::2])
data2 = [[-1, int(x)] if i % 2 else [i//2, int(x)] for i, x in enumerate(files)]
# print(f'{data=}\n{empty=}')
print(data2)

# rearrange
if not part2:
    final = []
    free = 0
    id, size = data.pop()

    while data:
        if free == 0:  # add from left
            leftid, leftsize = data.popleft()
            final.extend([leftid] * leftsize)
            free = empty.popleft()
        
        elif size <= free:
            final.extend([id] * size)
            free -= size
            id, size = data.pop()
        
        elif size > free:
            final.extend([id] * free)
            size -= free
            free = 0
            
    final.extend([id] * size)
    
    print(final)

else: # part2
    ans = 0
    i = len(data2) - 1
    while i > 0:
        id, size = data2[i]
        if id >= 0:
            for j in range(i):
                left_id, left_size = data2[j]
                if left_id == -1 and left_size >= size:
                    data2[i] = [-1, size]
                    data2[j] = [-1, left_size - size]
                    data2.insert(j, [id, size])
                    break
        i -= 1
        
    print(data2)

            
# calculate checksum
if not part2:
    ans = 0
    for i, val in enumerate(final):
        ans1 += i * val
        
    print(f'Part 1 answer is {ans}')
    
# test val = 1928
# test blocks: 0099811188827773336446555566
# 3024234126231 is too low
# 6310675819476 is correct

if part2:
    ans = 0
    i = 0
    for id, size in data2:
        if id > 0:
            j = sum(range(i, i + size))
            ans += j * id
        i += size
        
    print(f'Part 2 answer is {ans}')
# 6335972980679 is correct