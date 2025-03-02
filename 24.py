# Advent of Code 2024 - Day 24

test = False

if test:
    filename = 'test24.txt'
    digits = 12
    input_digits = 5
else:
    filename = 'data24.txt'
    digits = 45
    input_digits = 45

states: dict[str, int] = dict()
circuits: dict[str, list[str]] = dict()


with open(filename) as f:
    for line in f.readlines():
        if ':' in line:
            key, value = line.strip().split(':')
            states[key] = int(value)
        if '->' in line:
            input1, op, input2, _, node = line.strip().split(' ')
            circuits[node] = [op, input1, input2]
            a, b = sorted([input1, input2])


def get_value(node: str) -> int:
    if node in states:
        return states[node]
    
    try:
        op, input1, input2 = circuits[node]
    except KeyError:
        raise ValueError(f'get_value(): Unknown circuit: {node}')

    if op == 'AND':
        ans = get_value(input1) & get_value(input2)
    if op == 'OR':
        ans = get_value(input1) | get_value(input2)
    if op == 'XOR':
        ans = get_value(input1) ^ get_value(input2)

    return ans
    
    raise ValueError(f'Bad circuit syntax: {node}: {circuits[node]}')

def result() -> int:
    values = []
    z_nodes = ['z' + f'{str(i):>02}' for i in range(digits, -1, -1)]

    for node in z_nodes:
        values.append(str(get_value(node)))

    return int(''.join(values), base=2)

print(f'Part 1 answer: {result()}')
# 5704 too low
# 11408 too low
# 38869984335432 is correct

# Part 2
# Determine the values of x & y
x_nodes = ['x' + f'{str(i):>02}' for i in range(input_digits-1, -1, -1)]
y_nodes = ['y' + f'{str(i):>02}' for i in range(input_digits-1, -1, -1)]

def swap(node1: str, node2: str) -> None:
    circuits[node1], circuits[node2] = circuits[node2], circuits[node1]

#found swaps by hand
swap('qjb', 'gvw')
swap('z15', 'jgc')
swap('z22', 'drg')
swap('z35', 'jbp')

# part2 answer: drg,gvw,jbp,jgc,qjb,z15,z22,z35 is correct!

def validate(digit: int, carryin: str) -> bool:
    # x, y, carryin
    logics = ((0,0,0), (0,0,1), (0,1,0), (1,0,0), (0,1,1), (1,0,1), (1,1,0), (1,1,1))

    x_in = f'x{str(digit):>02}'
    y_in = f'y{str(digit):>02}'
    z_out = f'z{str(digit):>02}'

    for x, y, carry in logics:
        states[x_in] = x
        states[y_in] = y
        states[carryin] = carry

        result = (x ^ y) ^ carry

        if get_value(z_out) != result:
            print(f'Failed on digit {digit} with {x=} {y=} {carry=} -> {get_value(z_out)} {carryin=}')
            del states[carryin]
            return False
    
    del states[carryin]

    return True

def get_inputs(wire: str) -> set[str]:
    if wire in states:
        return {wire}
    
    return set(circuits[wire][1:]) | get_inputs(circuits[wire][1]) | get_inputs(circuits[wire][2])

def get_output(wire1, wire2, op) -> str:
    for outwire, circuit in circuits.items():
        if circuit[0] == op and set(circuit[1:]) == {wire1, wire2}:
            return outwire

    raise KeyError(f'get_output(): No circuit found for {wire1} {wire2} {op} ->')
    
# u_wires = [0] * input_digits
# w_wires = [0] * input_digits
# carryins = [0] * (input_digits + 1)
# unassigned = set()

# u, v, w = '', '', ''

# for outwire, circuit in circuits.items():
#     if outwire[0] not in 'xyz':
#         unassigned.add(outwire)

#     if circuit[1][0][0] in 'xy' and  circuit[2][0][0] in 'xy':
#         i = int(circuit[1][1:])
#         if circuit[0] == 'XOR':
#             u_wires[i] = outwire

#         if circuit[0] == 'AND':
#             w_wires[i] = outwire

#     if outwire.startswith('z'):
#         i = int(outwire[1:])
#         carryins[i] = circuit

# for i in range(input_digits):
#    print(f'x{i:02} XOR y{i:02} -> {u_wires[i]}; x{i:02} AND y{i:02} -> {and_wires[i]}; {carryins[i]} -> z{i:02}')

# print(f'{carryins[45]} -> z45')
    
# check each circuit

carryin = 'nvv' 

i: int = 1

while i <= input_digits:
    x, y = f'x{str(i):>02}', f'y{str(i):>02}'
    input_wires = get_inputs(f"z{str(i):>02}") - get_inputs(f"z{str(i-1):>02}")
    if validate(i, carryin):
        print(f'Validated z{str(i):>02}, {carryin=}')

        # find carryout
        #find u
        u = get_output(x, y, 'XOR')
        
        try:
            # find v
            v = get_output(u, carryin, 'AND')

            # find w
            w = get_output(x, y, 'AND')

            # find carryout
            carryin = get_output(v, w, 'OR')

        except KeyError as e:
            print(f'Failed to find carryout for z{str(i):>02}, {e}')
            break

        print(f'{i}: {u=} {v=} {w=} carry={carryin}')

        i += 1

    else:
        print(f'Failed on {i}')
        print(f'{carryin=}')
        print(f'{input_wires=}')
        break

