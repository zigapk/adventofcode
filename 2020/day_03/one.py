forest = []
with open('in', 'r') as f:
    for line in f.readlines():
        forest.append(list(line[:-1]))

x = 0
y = 0
count = 0

while y < len(forest):
    if forest[y][x] == '#':
        count += 1

    # move 3 right, down 1
    x += 3
    y += 1

    # circular nature of the forest
    x %= len(forest[0])

print(count)
