from collections import deque

def knot_hash(h):
    size = 256
    skip_size = 0
    data = [i for i in range(size)]
    current = 0

    lengths = list(map(ord, h))
    lengths += [17, 31, 73, 47, 23]

    for _ in range(64):
        for i in lengths:
            buff = []
            for j in range(current, current + i):
                buff.append(data[j % size])

            buff = buff[::-1]

            for j in range(len(buff)):
                data[(j + current) % size] = buff[j]

            current += i + skip_size
            current %= size
            skip_size += 1

    d_hash = ''
    for i in range(16):
        block = 0
        for j in range(i * 16, i* 16 + 16):
            block ^= data[j]
        d_hash += hex(block)[2:].zfill(2)
    return d_hash

key = input()

s1 = 0
disk = []

for i in range(128):
    hex_hash = knot_hash('{}-{}'.format(key, i))
    line = ''.join(['{0:04b}'.format(int(i, base=16)) for i in hex_hash])
    disk.append(list(line))
    s1 += line.count('1')

print(s1)


s2 = 0
possible_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
seen = set()
for y in range(128):
    for x in range(128):
        if (x, y) in seen:
            continue
        if disk[y][x] == '0':
            continue

        s2 += 1
        que = deque()
        que.append((x, y))
        seen.add((x, y))

        while len(que) > 0:
            x_1, y_1 = que.popleft()
            for move in possible_moves:
                x_2 = x_1 + move[0]
                y_2 = y_1 + move[1]
                if x_2 < 0 or x_2 > 127 or y_2 < 0 or y_2 > 127:
                    continue
                if disk[y_2][x_2] == '0':
                    continue
                if (x_2, y_2) in seen:
                    continue
                seen.add((x_2, y_2))
                que.append((x_2, y_2))
print(s2)
