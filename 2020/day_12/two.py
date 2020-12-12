import math

# direction vectors
north = (0, 1)
south = (0, -1)
east = (1, 0)
west = (-1, 0)
waypoint = (10, 1)

x, y = 0, 0

with open('in', 'r') as f:
    for line in f.readlines():
        arg = int(line[1:])
        cmd = line[:1]

        if cmd == 'F':
            x, y = x + waypoint[0] * arg, y + waypoint[1] * arg
        elif cmd == 'R' or cmd == 'L':
            # rotate waypoint
            if cmd == 'R':
                arg = -arg

            arg = arg * math.pi / 180  # convert to radians

            # rotate direction vector
            waypoint = (
                math.cos(arg) * waypoint[0] - math.sin(arg) * waypoint[1],
                math.sin(arg) * waypoint[0] + math.cos(arg) * waypoint[1]
            )

            # round
            waypoint = (round(waypoint[0]), round(waypoint[1]))
        elif cmd == 'N':
            waypoint = (waypoint[0] + arg * north[0], waypoint[1] + arg * north[1])
        elif cmd == 'S':
            waypoint = (waypoint[0] + arg * south[0], waypoint[1] + arg * south[1])
        elif cmd == 'E':
            waypoint = (waypoint[0] + arg * east[0], waypoint[1] + arg * east[1])
        elif cmd == 'W':
            waypoint = (waypoint[0] + arg * west[0], waypoint[1] + arg * west[1])

print(abs(x) + abs(y))
