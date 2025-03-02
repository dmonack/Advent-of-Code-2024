from collections import defaultdict

mapp = defaultdict(list)

with open('help17.txt', 'r') as f:
    for line in f.readlines():
        i = line.find(',')
        inn, out = line[2:i], line[i+3:-2]
        out = out.replace(', ', '')
        mapp[out].append(inn)
        
while (i := input('? ')) != 'q':
    print(mapp[i])