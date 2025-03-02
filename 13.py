# Advent of Code 2024 - Day 13

from itertools import batched

part2 = True
ROUND_FACTOR: int = 0


if part2: # part2
    ADJUSTMENT: int = 10000000000000
else:
    ADJUSTMENT: int = 0
    
class Machine:
    def __init__(self, ax: int, ay: int, bx: int, by: int, prize_x: int, prize_y: int):
        self.vector_a = f'{ax}, {ay}'
        self.vector_b = f'{bx}, {by}'
        self.prize = f'{prize_x}, {prize_y}'
        slope_a, slope_b = ay / ax, by / bx
        intercept_b = prize_y - (slope_b * prize_x)
        self.x = round(intercept_b / (slope_a - slope_b), ROUND_FACTOR)
        self.y = round(slope_a * self.x, ROUND_FACTOR) 
        
        self.valid = (self.x % ax == 0 and
                 self.y % ay == 0 and
                 (prize_x - self.x) % bx == 0 and
                 (prize_y - self.y) % by == 0)
        
        self.a = self.x // ax
        self.b = (prize_x - self.x) // bx
        
        if not self.valid:
            self.price = 0
        else:
            self.price = int(3 * self.a + self.b)
    
    def __repr__(self):
        return f'''Machine A: {self.valid}, Prize: {self.prize}; vectA: {self.vector_a}; vectB: {self.vector_b};
            A: {self.a}x, B: {self.b}x;
            Price: {self.price}
            Intercept: {self.x}, {self.y}
            
        '''

with open('data13.txt', 'r') as f:
    lines = f.readlines()
    
machines = []
for a, b, p, _ in batched(lines, 4):
    ax, ay = int(a[12:14]), int(a[18:])
    bx, by = int(b[12:14]), int(b[18:])
    left, right = p.split(',')
    px = int(left.split('=')[1]) + ADJUSTMENT
    py = int(right.split('=')[1]) + ADJUSTMENT
    machines.append(Machine(ax, ay, bx, by, px, py))
    
ans = sum(x.price for x in machines)

print(machines)

if not part2:
    print(f'Part 1 answer is {ans}')
    # 25587 is too low
    # 28262 is right!

else:
    print(f'Part 2 answer is {ans}')
    # 51021798653097 is too low
    # 65561284711399 is too low
    # 101406661266314 is correct!