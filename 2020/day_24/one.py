from collections import defaultdict

with open('in', 'r') as f:
    lines = [i.strip() for i in f.readlines()]

vectors = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (1, -1),
    'sw': (0, -1),
    'ne': (0, 1),
    'nw': (-1, 1),
}

tiles = defaultdict(bool)


def follow_path(line):
    x, y = 0, 0

    while len(line) > 0:
        if len(line) >= 2 and line[:2] in vectors:
            direction, line = line[:2], line[2:]
        else:
            direction, line = line[:1], line[1:]

        vector = vectors[direction]
        x += vector[0]
        y += vector[1]
    return x, y


for line in lines:
    x, y = follow_path(line)
    tiles[(x, y)] = not tiles[(x, y)]

count = 0
for k in tiles.keys():
    if tiles[k]:
        count += 1

print(count)
