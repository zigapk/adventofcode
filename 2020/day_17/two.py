from collections import defaultdict

grid = defaultdict(bool)

with open('in', 'r') as f:
    lines = f.readlines()

min_x = 0
min_y = 0
min_z = 0
min_w = 0
max_x = 0
max_y = 0
max_z = 0
max_w = 0


for y in range(len(lines)):
    line = lines[y]
    max_y = y
    for x in range(len(line)):
        grid[(x, y, 0, 0)] = line[x] == '#'
        max_x = x


def count_active_neighbours(center_x, center_y, center_z, center_w):
    count = 0
    for x in range(center_x - 1, center_x + 2):
        for y in range(center_y - 1, center_y + 2):
            for z in range(center_z - 1, center_z + 2):
                for w in range(center_w - 1, center_w + 2):
                    if x == center_x and y == center_y and z == center_z and w == center_w:
                        continue

                    if grid[(x, y, z, w)]:
                        count += 1

    return count


def cycle():
    global min_x, min_y, max_x, max_y, min_z, max_z, min_w, max_w
    result = defaultdict(bool)

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    active_neighbours = count_active_neighbours(x, y, z, w)
                    set_as_active = False

                    if grid[(x, y, z, w)]:
                        if active_neighbours == 2 or active_neighbours == 3:
                            set_as_active = True
                    else:
                        if active_neighbours == 3:
                            set_as_active = True

                    if set_as_active:
                        result[(x, y, z, w)] = True

                        if x < min_x:
                            min_x = x
                        if y < min_y:
                            min_y = y
                        if z < min_z:
                            min_z = z
                        if w < min_w:
                            min_w = w
                        if x > max_x:
                            max_x = x
                        if y > max_y:
                            max_y = y
                        if z > max_z:
                            max_z = z
                        if w > max_w:
                            max_w = w

    return result


for _ in range(6):
    grid = cycle()

print(len(grid))
