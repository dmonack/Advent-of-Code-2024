# Advent of Code 2024 - Day 5
from collections import defaultdict, Counter
from functools import cmp_to_key
from itertools import permutations

rules = defaultdict(set)
updates = []

with open("data05.txt") as f:
    for line in f.readlines():
        if '|' in line:
            a, b = line.split('|')
            rules[int(a)].add(int(b))

        elif ',' in line:
            updates.append(tuple(int(x) for x in line.split(',')))

# print(updates)

def validUpdate(update: tuple[int]|list[int])->bool:
    for i, item in enumerate(update):
        for subsq in update[i+1:]:
            if item in rules[subsq]:
                return False

    return True

def compare(a, b) -> int:
    if b in rules[a]:
        return 1
    if a in rules[b]:
        return -1
    return 0

def reorder(update: list[int]) -> list[int]:
    correct = []
    seen = set()
    while True:
        while update[-1] in seen:
            correct.append(update.pop())
            if not update:
                return correct[::-1]
            
        curr = update[-1]
        seen.add(curr)
        
        for node in rules[curr]:
            if node in update and node not in seen:
                update.remove(node)
                update.append(node)

def reorder2(pages: list[int]) -> list[int]:
    print("reorder2")
    i = 0
    j = len(pages)-1
    while i < len(pages):
        print(i, j)

        if pages[i] in rules[j]:
            print(f"swap {pages[i]} & {pages[j]}")
            pages[j], pages[i] = pages[i], pages[j]
            j = len(pages) - 1
            print(pages)
            
        elif i == j:
            i += 1
            j = len(pages) - 1
            
        else:
            j -= 1
            
    print(f"Corrected? {validUpdate(pages)}")
    return pages

def reorder3(pages: list[int]) -> list[int]:
    return sorted(pages, key = cmp_to_key(compare))

def reorder4(pages: list[int]|tuple[int]) -> tuple[int]: 
    # O(n!) hope you finish before the heat death of the universe
    for e in permutations(pages):
        if validUpdate(e):
            return e
        
def reorder5(pages: list[int]) -> list[int]:
    ordered = []
    count: Counter = Counter(pages)
    for item in pages:
        count += Counter(filter(lambda x: x in pages, rules[item]))
        
    while pages:
        for val in pages:
            if count[val] == 1:
                ordered.append(val)
                count -= Counter(rules[val])
                pages.remove(val)
                
    return ordered
    
ans = 0
ans2 = 0
for update in updates:
    middle_i = len(update) // 2
    if validUpdate(update):
        ans += update[middle_i]
        print(f"***VALID: {update}, {ans=}")

    else:  # correct the order and add to ans2
        corrected = reorder5(list(update))
        ans2 += corrected[middle_i]
        print(f'{corrected} {("!!!!!! ERROR !!!!!!", "_true_")[validUpdate(corrected)]} [{corrected[middle_i]}] {ans2=}')

print(f"Part 1 answer: {ans}")
# 5747 is correct

print(f"Part 2 answer: {ans2}")
# 11612 is too high
# 11520 is too high
# 11940 is too high
# 6193 is not right
# 5773 wrong
# 5439 wrong
# 5379 wrong
# 5836 wrong
# 5502 is correct