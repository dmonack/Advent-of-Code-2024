# Advent of Code 2024 - Day 19

from functools import lru_cache

patterns = []
with open('data19.txt', 'r') as f:
    towels = f.readline().rstrip().split(', ')
    f.readline()
    for line in f.readlines():
        patterns.append(line.rstrip())
        
towels.sort(key = len, reverse = True)
# print(towels, patterns)

@lru_cache
def possible(pat: str)->int:
    if not pat:
        return 1
    
    ret = 0
    for towel in towels:
        if pat.startswith(towel):
            ret += possible(pat[len(towel):])
        
    return ret
        
      
if __name__ == '__main__':
    ans1, ans2 = 0, 0
    for pattern in patterns:
        if (valid := possible(pattern)):
            ans1 += 1
            ans2 += valid
        print(f'{pattern}: {valid}')
        
    print(f'Part 1 answer is {ans1}')
    # 296 is correct
    
    print(f'Part 2 answer is {ans2}')
    # 619970556776002 is correct
        