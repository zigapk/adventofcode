from collections import deque
import re

tiles = {}

lines = [i.strip() for i in open('in', 'r').readlines()]

for i in range(0, len(lines) + 1, 12):
    tile_id = int(lines[i].split()[1][:-1])

    new_tile = []
    for j in range(i + 1, i + 11):
        new_tile.append(lines[j])

    tiles[tile_id] = new_tile


def rotate(tile):
    # rotates left
    res = []
    for x in range(9, -1, -1):
        current = ''
        for y in range(0, 10):
            current += tile[y][x]
        res.append(current)

    return res


def flip(tile):
    return tile[::-1]


def get_right_edge(tile):
    res = ''
    for line in tile:
        res += line[-1]
    return res


def get_left_edge(tile):
    res = ''
    for line in tile:
        res += line[0]
    return res


def get_top_edge(tile):
    return tile[0]


def get_bottom_edge(tile):
    return tile[-1]


def match_left_edge(tile_to_be_skipped, edge):
    # try to match each tile
    for k in tiles.keys():
        if k == tile_to_be_skipped:
            continue  # skip the current tile

        tile = tiles[k]

        # try rotating and flipping the tile to find the one that matches it
        for _ in range(4):
            if get_left_edge(tile) == edge:
                return k, tile

            flipped = flip(tile)
            if get_left_edge(flipped) == edge:
                return k, flipped

            tile = rotate(tile)

    return None, None


def match_right_edge(tile_to_be_skipped, edge):
    match_id, match = match_left_edge(tile_to_be_skipped, edge)

    if match_id is not None:
        return match_id, rotate(rotate(flip(match)))

    return None, None


def match_bottom_edge(tile_to_be_skipped, edge):
    match_id, match = match_left_edge(tile_to_be_skipped, edge)

    if match_id is not None:
        return match_id, rotate(match)

    return None, None


def match_top_edge(tile_to_be_skipped, edge):
    match_id, match = match_left_edge(tile_to_be_skipped, edge)

    if match_id is not None:
        return match_id, rotate(rotate(rotate(match)))

    return None, None


# start with the first tile
tile_id = list(tiles.keys())[2]
tile = tiles[tile_id]

image = {}
image[(0, 0)] = tile, tile_id

q = deque()
# x, y, id, edge, dx, dy
q.append((0, 0, tile_id, get_left_edge(tile), -1, 0))
q.append((0, 0, tile_id, get_right_edge(tile), 1, 0))
q.append((0, 0, tile_id, get_bottom_edge(tile), 0, -1))
q.append((0, 0, tile_id, get_top_edge(tile), 0, 1))

while len(q) > 0:
    x, y, tile_id, edge, dx, dy = q.popleft()

    if (x + dx, y + dy) in image:
        continue  # this tile was already resolved

    next, next_id = None, None

    # try to match each direction
    if dx == -1:
        next_id, next = match_right_edge(tile_id, edge)
    elif dx == 1:
        next_id, next = match_left_edge(tile_id, edge)
    elif dy == 1:
        next_id, next = match_bottom_edge(tile_id, edge)
    elif dy == -1:
        next_id, next = match_top_edge(tile_id, edge)

    if next_id is None:
        continue

    image[(x + dx, y + dy)] = (next, next_id)

    q.append((x + dx, y + dy, next_id, get_left_edge(next), -1, 0))
    q.append((x + dx, y + dy, next_id, get_right_edge(next), 1, 0))
    q.append((x + dx, y + dy, next_id, get_bottom_edge(next), 0, -1))
    q.append((x + dx, y + dy, next_id, get_top_edge(next), 0, 1))

min_x = min([i[0] for i in image.keys()])
min_y = min([i[1] for i in image.keys()])
max_x = max([i[0] for i in image.keys()])
max_y = max([i[1] for i in image.keys()])

monster = []
monster += [(m.start(), 0) for m in re.finditer('#', '                  # ')]
monster += [(m.start(), 1) for m in re.finditer('#', '#    ##    ##    ###')]
monster += [(m.start(), 2) for m in re.finditer('#', ' #  #  #  #  #  #   ')]


def count_monsters(src):
    res = 0

    for y in range(len(src)):
        for x in range(len(src[0])):
            contains = True
            for dx, dy in monster:
                x1, y1 = x + dx, y + dy
                if x1 < 0 or x1 >= len(src[0]) or y1 < 0 or y1 >= len(src):
                    contains = False
                    break

                if src[y1][x1] != '#':
                    contains = False
                    break

            if contains:
                res += 1
    return res


l = len(image[(min_x, min_y)][0]) - 2

img = []
for y in range(max_y, min_y - 1, -1):
    img += [''] * l

    for x in range(min_x, max_x + 1):
        for i in range(1, l + 1):
            img[len(img) - l + i - 1] += image[(x, y)][0][i][1:-1]

# for line in img:
#     print(line)

for _ in range(4):
    n = count_monsters(img)
    if n > 0:
        print(n)
        break

    flipped = flip(img)

    n = count_monsters(flipped)
    if n > 0:
        print(n)
        break

    img = rotate(img)
