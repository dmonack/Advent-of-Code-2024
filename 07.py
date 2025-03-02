# Advent of Code 2024 - Day 7

PART2 = True
equations = []

with open("data07.txt") as f:
    for line in f.readlines():
        sum, nums = line.split(':')
        equations.append([int(sum)] + [int(x) for x in nums.split()])
        
ans = 0

for sum, *vals in equations:
    # print(f'\n+++ {sum} {vals} +++')
    possibles = [vals.pop(0)]
    while vals:
        curr = vals.pop(0)
        # print(possibles)
        for _ in range(len(possibles)):
            x = possibles.pop(0)
            if (added := curr + x) <= sum:
                possibles.append(added)
            if (multed := curr * x) <= sum:
                possibles.append(multed)
                
            if PART2: # add concatenated numbers
                possibles.append(int(str(x) + str(curr)))
            
    if sum in possibles:
        ans += sum
        # print('!!')
    # print(f"{sum = } {possibles} : {ans1 = }")
        
print(f"Answer is {ans}")
# Part 1:
# 133_850_494_205 too low!
# 7,885,693,428,401 is right!

# Part 2:
# 348,360,680,516,005 is right!