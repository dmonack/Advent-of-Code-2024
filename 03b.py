# Advent of Code 2024 - Puzzle 3 - part II

with open("data03.txt") as f:
    data = f.read()

ans = 0

# scrub the data of all the don'ts
while "don't" in data:
    left = data.find("don't()")
    right = data.find("do()", left + 6)
    if right == -1:
        data = data[:left]
    else:
        data = data[:left] + '#' + data[right + 4:]


left = data.find('mul(')

while left >= 0:
    left += 4
    right = left
    while data[right] in '0123456789,':
        right += 1

    if data[right] == ')' and data[left:right].count(',') == 1:
        a, b = data[left:right].split(',')
        ans += int(a) * int(b)

    left = data.find('mul(', right) 
            

print(f'Part 2 answer: {ans}')

# 98729041 is correct