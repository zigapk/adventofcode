from collections import defaultdict

grid = defaultdict(bool)

with open('in', 'r') as f:
    lines = f.readlines()

min_x = 0
min_y = 0
min_z = 0
max_x = 0
max_y = 0
max_z = 0

for y in range(len(lines)):
    line = lines[y]
    max_y = y
    for x in range(len(line)):
        grid[(x, y, 0)] = line[x] == '#'
        max_x = x


def count_active_neighbours(center_x, center_y, center_z):
    count = 0
    for x in range(center_x - 1, center_x + 2):
        for y in range(center_y - 1, center_y + 2):
            for z in range(center_z - 1, center_z + 2):
                if x == center_x and y == center_y and z == center_z:
                    continue

                if grid[(x, y, z)]:
                    count += 1

    return count


def cycle():
    global min_x, min_y, max_x, max_y, min_z, max_z
    result = defaultdict(bool)

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                active_neighbours = count_active_neighbours(x, y, z)
                set_as_active = False

                if grid[(x, y, z)]:
                    if active_neighbours == 2 or active_neighbours == 3:
                        set_as_active = True
                else:
                    if active_neighbours == 3:
                        set_as_active = True

                if set_as_active:
                    result[(x, y, z)] = True

                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                    if z < min_z:
                        min_z = z
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y
                    if z > max_z:
                        max_z = z

    return result


for _ in range(6):
    grid = cycle()

print(len(grid))
