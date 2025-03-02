# Advent of Code 2024 - Puzzle 4

with open("data04.txt") as f:
    puzzle = f.readlines()

width = len(puzzle[0]) - 1
height = len(puzzle)

ans = 0

directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

for column in range(width):
    for row in range(height):
        for x, y in directions:

            #check for leaving board
            if (0 <= column + (3 * y) < width and
                    0 <= row + (3 * x) < height):

                letters = [puzzle[column + i * y][row + i * x] for i in range(4)]

                if letters == ['X', 'M', 'A', 'S']:
                    ans += 1

                # print(f"{column}, {row} ({y}, {x}), {''.join(letters)}, total: {ans}")                   

print(f"Part 1 answer: {ans}") 

# 2662 is correct

ans2 = 0
valids = [['M', 'A', 'S'], ['S', 'A', 'M']]

for column in range(1, width-1):
    for row in range(1, height-1):
        word1 = [puzzle[column-1][row+1], puzzle[column][row], puzzle[column+1][row-1]]
        word2 = [puzzle[column+1][row+1], puzzle[column][row], puzzle[column-1][row-1]]

        if word1 in valids and word2 in valids:
            ans2 += 1

        # print(f"{column}, {row}, {word1}, {word2}, {ans2=}")

print(f"Part 2 answer: {ans2}")

# 2034 is correct