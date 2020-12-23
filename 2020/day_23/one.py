with open('in', 'r') as f:
    cups = list(map(int, f.readline().strip()))


def pick_cups(cups, i):
    a, b = i + 1, i + 4
    a, b = a % len(cups), b % len(cups)

    inverted = a > b
    if inverted:
        picked_a, cups, picked_b = cups[a:], cups[b:a], cups[:b]
        return cups, picked_a + picked_b
    else:
        cups_a, picked, cups_b = cups[:a], cups[a:b], cups[b:]
        return cups_a + cups_b, picked


def find_destination(cups, n):
    res = n - 1
    while res not in cups:
        res -= 1
        if res < min(cups):
            res = max(cups)
    return res


def insert(cups, picked, index):
    return cups[:index + 1] + picked + cups[index + 1:]


current = cups[0]
for _ in range(100):
    # print(cups, current)
    cups, picked = pick_cups(cups, cups.index(current))

    dest = find_destination(cups, current)
    # print(cups, picked, dest)
    # input()

    cups = insert(cups, picked, cups.index(dest))
    i = cups.index(current)
    i += 1
    i %= len(cups)
    current = cups[i]

cups = cups[cups.index(1):] + cups[:cups.index(1)]
print(''.join(map(str, cups))[1:])
