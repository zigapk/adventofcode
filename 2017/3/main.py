import sys

def p(mem, a, field_length=3):
    for y in range(len(mem) // 2 + a, len(mem) // 2 - a - 1, -1):
        for x in range(len(mem) // 2 - a, len(mem) // 2 + a + 1):
            s = str(mem[x][y])
            while len(s) < field_length:
                s = ' ' + s
            print(s, end='')
        print('')

n = int(input())

# first part

mem = [[0 for i in range(1001)] for j in range(1001)]
x, y = len(mem) // 2, len(mem) // 2
a = 1
mem[x][y] = a
steps = 1

done = False
while not done:
    x += 1
    a += 1
    mem[x][y] = a

    for i in range(steps):
        if a == n: break
        y += 1
        a += 1
        mem[x][y] = a
    for i in range(steps + 1):
        if a == n: break
        x -= 1
        a += 1
        mem[x][y] = a
    for i in range(steps + 1):
        if a == n: break
        y -= 1
        a += 1
        mem[x][y] = a
    for i in range(steps + 1):
        if a == n: break
        x += 1
        a += 1
        mem[x][y] = a

    if n == a: done = True
    steps += 2
print(abs(x-len(mem) // 2) + abs(y - len(mem) // 2))

# print()
# print()
# print()
# p(mem, 5)

# part two - a dirty brute force

def sum_around(mem, x, y):
    global n
    s = mem[x-1][y] + mem[x-1][y-1] + mem[x][y-1] + mem[x+1][y-1] + mem[x+1][y] + mem[x+1][y + 1] + mem[x][y + 1] + mem[x-1][y + 1]
    if s > n:
        print(s)
        sys.exit(0)
    return s

mem = [[0 for i in range(1001)] for j in range(1001)]
x, y = len(mem) // 2, len(mem) // 2
a = 1
mem[x][y] = a
steps = 1

while True:
    x += 1
    a += 1
    mem[x][y] = sum_around(mem, x, y)

    for i in range(steps):
        y += 1
        a += 1
        mem[x][y] = sum_around(mem, x, y)
    for i in range(steps + 1):
        x -= 1
        a += 1
        mem[x][y] = sum_around(mem, x, y)
    for i in range(steps + 1):
        y -= 1
        a += 1
        mem[x][y] = sum_around(mem, x, y)
    for i in range(steps + 1):
        x += 1
        a += 1
        mem[x][y] = sum_around(mem, x, y)

    steps += 2
    
