def safe(data: list[str])->bool:
    a, b = int(data[0]), int(data[1])
    diff = abs(b - a)
    if diff < 1 or diff > 3:
        return False

    for val in data[2:]:
        c = int(val)
        if (b>a and b>c) or (b < a and b < c):
            return False

        diff = abs(c-b)
        if diff < 1 or diff > 3:
            return False
        
        a, b = b, c

    return True

def safe2(data: list[str])->bool:
    for i in range(len(data)):
        if safe(data[:i] + data[i+1:]):
            return True

    return False


ans = 0
ans2 = 0
with open("data02.txt") as f:
    for line in f.readlines():
        if safe(line.split()):
            ans += 1

        if safe2(line.split()):
            ans2 += 1

print(f"Part 1 answer: {ans}")

# 411 correct


print(f"Part 2 answer: {ans2}")

#465 correct