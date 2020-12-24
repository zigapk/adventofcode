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


def count_adjacent_black_tiles(x, y, tiles):
    count = 0
    for vector in vectors.values():
        if tiles[(x + vector[0], y + vector[1])]:
            count += 1
    return count


def evolve(tiles, min_x, min_y, max_x, max_y):
    result = defaultdict(bool)
    new_min_x = min_x
    new_min_y = min_y
    new_max_x = max_x
    new_max_y = max_y

    for x in range(min_x - 3, max_x + 4):
        for y in range(min_y - 3, max_y + 4):
            c = count_adjacent_black_tiles(x, y, tiles)

            if tiles[(x, y)] and (c > 0 and c <= 2) or not tiles[(x, y)] and c == 2:
                result[(x, y)] = True

                if x < new_min_x:
                    new_min_x = x
                if y < new_min_y:
                    new_min_y = y
                if x > new_max_x:
                    new_max_x = x
                if y > new_max_y:
                    new_max_y = y

    return result, new_min_x, new_min_y, new_max_x, new_max_y


min_x, min_y, max_x, max_y = 0, 0, 0, 0
for line in lines:
    x, y = follow_path(line)
    tiles[(x, y)] = not tiles[(x, y)]

    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

for i in range(100):
    tiles, min_x, min_y, max_x, max_y = evolve(tiles, min_x, min_y, max_x, max_y)

count = 0
for k in tiles.keys():
    if tiles[k]:
        count += 1

print(count)
