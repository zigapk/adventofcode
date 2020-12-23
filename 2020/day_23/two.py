with open('in', 'r') as f:
    cups = list(map(int, f.readline().strip()))

i = max(cups)
while len(cups) < 1000000:
    i += 1
    cups.append(i)

data = [None for _ in range(1000000)]

for i in range(len(cups)):
    current = cups[i] - 1
    next = cups[(i + 1) % len(cups)] - 1
    data[current] = next

M = max(data)


def pick_cups(current, data):
    picked = []
    to_be_picked = data[current]
    for _ in range(3):
        picked.append(to_be_picked)
        to_be_picked = data[to_be_picked]

    data[current] = to_be_picked
    return data, picked


def find_destination(current, picked):
    a = current - 1
    while a in picked or a < 0:
        if a < 0:
            a = M
            continue
        a -= 1

    return a


def insert(dest, picked, data):
    data[picked[2]] = data[dest]
    data[dest] = picked[0]
    data[picked[0]] = picked[1]
    data[picked[1]] = picked[2]
    return data


def print_linked_list(data):
    seen = set()
    a = data[0]
    while True:
        if a in seen:
            break
        seen.add(a)
        print(a + 1, end=' ')
        a = data[a]
    print()


current = cups[0] - 1
for i in range(10000000):
    data, picked = pick_cups(current, data)

    dest = find_destination(current, picked)

    data = insert(dest, picked, data)
    current = data[current]

res = (data[0] + 1) * (data[data[0]] + 1)
print(res)
