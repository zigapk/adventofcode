count = 0

with open('in', 'r') as f:
    for line in f.readlines():
        a, b, passwd = line.split()

        m, M = map(int, a.split('-'))
        chr = b[0]

        occur = passwd.count(chr)
        if occur >= m and occur <= M:
            count += 1

print(count)
