moves = input().split(',')

line = list('abcdefghijklmnop')
seen = set()
seen.add('abcdefghijklmnop')

count = 0
while True:
    for move in moves:
        if move[0] == 's':
            for i in range(int(''.join(move[1:]))):
                line, c = line[:-1], line[-1]
                line.insert(0, c)
        if move[0] == 'x':
            a, b = list(map(int, ''.join(move[1:]).split('/')))
            buff = line[b]
            line[b] = line[a]
            line[a] = buff
        if move[0] == 'p':
            a, b = list(''.join(move[1:]).split('/'))
            for i in range(len(line)):
                if line[i] == b:
                    line[i] = a
                elif line[i] == a:
                    line[i] = b

    if count == 0:
        print('s1:', ''.join(line))
    else:
        if ''.join(line) in seen:
            break
    count += 1

for i in range(1000000000%(count+1)):
    for move in moves:
        if move[0] == 's':
            for i in range(int(''.join(move[1:]))):
                line, c = line[:-1], line[-1]
                line.insert(0, c)
        if move[0] == 'x':
            a, b = list(map(int, ''.join(move[1:]).split('/')))
            buff = line[b]
            line[b] = line[a]
            line[a] = buff
        if move[0] == 'p':
            a, b = list(''.join(move[1:]).split('/'))
            for i in range(len(line)):
                if line[i] == b:
                    line[i] = a
                elif line[i] == a:
                    line[i] = b

print('s2:', ''.join(line))
