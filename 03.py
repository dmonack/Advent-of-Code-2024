# Advent of Code 2024 - Puzzle 3

with open("data03.txt") as f:
    data = f.read()

ans = 0

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
            

print(f'Part 1 answer: {ans}')

# 181345830 is correct

