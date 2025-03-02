# Advent of Code 2024 - Day 17

global A, B, C, pointer, result
test= False

if test:
    A, B, C = 2024, 0, 0
    PROGRAM = [0,3,5,4,3,0]

else:
    A, B, C = 47006051, 0, 0
    PROGRAM = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
    
pointer = 0
result = []

def combo(n: int) -> int:
    global A, B, C, pointer, result
    if n < 4:
        return n
    elif n == 4:
        return A
    elif n == 5:
        return B
    elif n == 6:
        return C
    else:
        raise ValueError(f"Invalid value {n} for combo")

# opcode 0
def adv():
    global A, B, C, pointer, result
    A //= 2 ** combo(PROGRAM[pointer + 1])
    pointer += 2
    
# opcode 1
def bxl():
    global A, B, C, pointer, result
    B ^= PROGRAM[pointer + 1]
    pointer += 2
    
# opcode 2
def bst():
    global A, B, C, pointer, result
    B = combo(PROGRAM[pointer + 1] ) % 8
    pointer += 2
    
# opcode 3
def jnz():
    global A, B, C, pointer, result
    if A != 0:
        pointer = PROGRAM[pointer + 1]
    else:
        pointer += 2
        
# opcode 4
def bxc():
    global A, B, C, pointer, result
    B ^= C
    pointer += 2
    
# opcode 5
def out():
    global A, B, C, pointer, result
    result.append(combo(PROGRAM[pointer + 1]) % 8)
    pointer += 2
    
# opcode 6
def bdv():
    global A, B, C, pointer, result
    B = A // (2 ** combo(PROGRAM[pointer + 1]))
    pointer += 2    

# opcode 7
def cdv():
    global A, B, C, pointer, result
    C = A // (2 ** combo(PROGRAM[pointer + 1]))
    pointer += 2
    
opcodes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

while pointer < len(PROGRAM):
    # print(f"{pointer = } | opcode: {PROGRAM[pointer]}, {A=} {B=} {C=}")
    opcodes[PROGRAM[pointer]]()
    
print('Part 1 answer:', ','.join(map(str, result)))
# 6,2,7,2,3,1,6,0,5 is correct

# Part 2

def run(n: int) -> list:
    global A, B, C, pointer, result
    A = n
    B = 0
    C = 0
    pointer = 0
    result = []
    while pointer < len(PROGRAM):
        opcodes[PROGRAM[pointer]]()
    return result
    
q = ['']
ans2 = []
seen = set()

while q:
    curr = q.pop()
    seen.add(curr)
    print(q)
    if len(curr) == 16:
        ans2.append(curr)
        continue
    for i in range(0o1000):
        new = curr + oct(i)[2:]
        digit = len(new)
        if run(int(new, 8)) == PROGRAM[-digit:] and new not in seen:
            q.append(new)
                
print('Part 2 answer:', int(min(ans2), 8))

# Part 2
# 236548287712877 is correct