# Advent of Code 2024 - Day 21

from functools import lru_cache
from data21 import codes

numeric_pad = {'0': (0, 1), 'A': (0, 2),
               '1': (1, 0), '2': (1, 1), '3': (1, 2),
               '4': (2, 0), '5': (2, 1), '6': (2, 2),
               '7': (3, 0), '8': (3, 1), '9': (3, 2)}

def numeric_to_arrows(prev: str, next: str) -> list[str]:
    '''Converts keypresses to list of possible arrow presses.'''
    prev_y, prev_x = numeric_pad[prev]
    next_y, next_x = numeric_pad[next]

    if prev_x == 0 and next_y == 0:
        return ['>' * (next_x - prev_x) + 'v' * (prev_y - next_y) + 'A']
    
    if prev_y == 0 and next_x == 0:
        return ['^' * (next_y - prev_y) + '<' * (prev_x - next_x) + 'A']

    if next_x > prev_x:
        horizontal = '>' * (next_x - prev_x)
    else:
        horizontal = '<' * (prev_x - next_x)

    if next_y > prev_y:
        vertical = '^' * (next_y - prev_y)
    else:
        vertical = 'v' * (prev_y - next_y)

    if not horizontal:
        return [vertical + 'A']

    if not vertical:
        return [horizontal + 'A']

    return [horizontal + vertical + 'A', vertical + horizontal + 'A']

def convert(s: str) -> list[str]:
    '''Converts a code to string of arrow presses.'''

    result = []
    prev = 'A'
    for c in s:
        section = numeric_to_arrows(prev, c)
        section.sort(key = len)
        result.append(section[0])
        prev = c

    return result

def keypad(prev: str, k: str) -> list[str]:
    if prev == k:
        return ['A']
    
    conversions: dict[str, str] = {'<^': ['>^A'], '<v': ['>A'], '<>': ['>>A'], '<A': ['>>^A'], 
                                    'v^': ['^A'], 'v>': ['>A'], 'v<': ['<A'], 'vA': ['>^A', '^>A'],
                                    '>^': ['<^A', '^<A'], '>v': ['<A'], '><': ['<<A'], '>A': ['^A'],
                                    '^<': ['v<A'], '^v': ['vA'], '^>': ['v>A', '>vA'], '^A': ['>A'],
                                    'A<': ['v<<A'], 'A^': ['<A'], 'Av': ['<vA', 'v<A'], 'A>': ['vA']}
    
    return conversions[prev + k]

@lru_cache
def n_presses(digits: str, levels: int) -> int:
    '''For a codestring, returns the minimum presses for n keypads.'''
    ret: int = 0

    if levels == 0:
        # print(digits, end='')
        return len(digits)

    prev = 'A'
    for digit in digits:
        next_level = keypad(prev, digit)
        ret += min(map(lambda x: n_presses(x, levels - 1), next_level))
        prev = digit

    return ret


if __name__ == '__main__':
    ans1 = 0
    ans2 = 0
    for code in codes:
        presses = 0
        presses2 = 0
        prev = 'A'
        for button in code:
            
            presses += min(map(lambda x: n_presses(x, 2), numeric_to_arrows(prev, button)))
            presses2 += min(map(lambda x: n_presses(x, 25), numeric_to_arrows(prev, button)))
            prev = button

        print(f' : {code=}, {presses=} {presses2=}')
        ans1 += int(code[:3]) * presses
        ans2 += int(code[:3]) * presses2

    print(f'Part 1 answer is {ans1}')

    # 123096 is correct

    print(f'Part 2 answer is {ans2} {ans2:_}')
    # 96_926_960_556_912 is too low
    # 246_060_311_068_804 is too high
    # 175_343_041_201_758 is too high
    # 154_115_708_116_294 is wrong
    # 154_517_692_795_352 is correct
        