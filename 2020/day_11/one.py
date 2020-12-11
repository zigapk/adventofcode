grid = []

with open('in', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))


def count_adjacent_occupied_seats(x, y):
    count = 0

    # up
    if y >= 1 and grid[y - 1][x] == '#':
        count += 1
    # down
    if y < len(grid) - 1 and grid[y + 1][x] == '#':
        count += 1
    # left
    if x >= 1 and grid[y][x - 1] == '#':
        count += 1
    # right
    if x < len(grid[0]) - 1 and grid[y][x + 1] == '#':
        count += 1

    # left up
    if y >= 1 and x >= 1 and grid[y - 1][x - 1] == '#':
        count += 1
    # right up
    if y >= 1 and x < len(grid[0]) - 1 and grid[y - 1][x + 1] == '#':
        count += 1
    # left down
    if y < len(grid) - 1 and x >= 1 and grid[y + 1][x - 1] == '#':
        count += 1
    # right down
    if y < len(grid) - 1 and x < len(grid[0]) - 1 and grid[y + 1][x + 1] == '#':
        count += 1

    return count


def evolve_grid():
    # looking back, this should never have been be a one-liner
    return [
        [
            '.' if grid[y][x] == '.' else
            '#' if grid[y][x] == 'L' and count_adjacent_occupied_seats(x, y) == 0 else
            'L' if grid[y][x] == '#' and count_adjacent_occupied_seats(x, y) >= 4 else
            grid[y][x]
            for x in range(len(grid[0]))
        ]
        for y in range(len(grid))
    ]


def count_occupied_seats():
    return sum([sum([e == '#' for e in ln]) for ln in grid])


while True:
    new_grid = evolve_grid()

    if new_grid == grid:
        print(count_occupied_seats())
        break

    grid = new_grid
