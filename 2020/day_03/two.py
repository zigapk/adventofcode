forest = []
with open('in', 'r') as f:
    for line in f.readlines():
        forest.append(list(line[:-1]))


def count_trees(vector):
    x = 0
    y = 0
    count = 0

    while y < len(forest):
        if forest[y][x] == '#':
            count += 1

        # move 3 right, down 1
        x += vector[0]
        y += vector[1]

        # circular nature of the forest
        x %= len(forest[0])
    return count


vectors = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

res = 1
for v in vectors:
    res *= count_trees(v)

print(res)
