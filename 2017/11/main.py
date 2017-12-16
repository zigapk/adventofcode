import hexutil

hexgrid = hexutil.HexGrid(1000, 1000)
center = hexutil.Hex(0, 0)
x, y = 0, 0

s2 = 0
line = input().split(',')

for e in line:
    if e == 'n':
        x += 1
        y += 1
    elif e == 'nw':
        x -= 1
        y += 1
    elif e == 'sw':
        x -= 2
    elif e == 's':
        y -= 1
        x -= 1
    elif e == 'se':
        x += 1
        y -= 1
    elif e == 'ne':
        x += 2

    current = hexutil.Hex(x, y)
    distance = center.distance(current)
    if distance > s2: s2 = distance



current = hexutil.Hex(x, y)
s1 = center.distance(current)
print(s1)
print(s2)
