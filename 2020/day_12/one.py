import math

# direction vectors
north = (0, 1)
south = (0, -1)
east = (1, 0)
west = (-1, 0)
direction = (1, 0)

x, y = 0, 0

with open('in', 'r') as f:
    for line in f.readlines():
        arg = int(line[1:])
        cmd = line[:1]

        if cmd == 'F':
            x, y = x + direction[0] * arg, y + direction[1] * arg
        elif cmd == 'R' or cmd == 'L':
            # handle direction
            if cmd == 'R':
                arg = -arg

            arg = arg * math.pi / 180  # convert to radians

            # rotate direction vector
            direction = (
                math.cos(arg) * direction[0] - math.sin(arg) * direction[1],
                math.sin(arg) * direction[0] + math.cos(arg) * direction[1]
            )

            # round, because the turns are always square
            direction = (round(direction[0]), round(direction[1]))
        elif cmd == 'N':
            x, y = x + arg * north[0], y + arg * north[1]
        elif cmd == 'S':
            x, y = x + arg * south[0], y + arg * south[1]
        elif cmd == 'E':
            x, y = x + arg * east[0], y + arg * east[1]
        elif cmd == 'W':
            x, y = x + arg * west[0], y + arg * west[1]

print(abs(x) + abs(y))
