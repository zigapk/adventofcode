grid = []

with open('in', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))


def follow_vector(x, y, vector):
    new_x, new_y = x + vector[1], y + vector[0]

    if new_x < 0 or new_x >= len(grid[0]):
        return 0

    if new_y < 0 or new_y >= len(grid):
        return 0

    if grid[new_y][new_x] == '#':
        return 1
    elif grid[new_y][new_x] == 'L':
        return 0

    return follow_vector(new_x, new_y, vector)


def count_adjacent_occupied_seats(x, y):
    count = 0

    vectors = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, -1),  # down left
        (1, 1),  # down right
    ]

    for v in vectors:
        count += follow_vector(x, y, v)

    return count


def evolve_grid():
    # looking back, this should never have been be a one-liner
    return [
        [
            '.' if grid[y][x] == '.' else
            '#' if grid[y][x] == 'L' and count_adjacent_occupied_seats(x, y) == 0 else
            'L' if grid[y][x] == '#' and count_adjacent_occupied_seats(x, y) >= 5 else
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
