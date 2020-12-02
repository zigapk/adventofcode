count = 0

with open('in', 'r') as f:
    for line in f.readlines():
        a, b, passwd = line.split()

        m, M = map(int, a.split('-'))
        chr = b[0]

        if sum([passwd[m - 1] == chr, passwd[M - 1] == chr]) == 1:
            count += 1

print(count)
