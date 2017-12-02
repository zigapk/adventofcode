import fileinput

lines = []

for line in fileinput.input():
    lines.append(list(map(int, line.split())))

# part 1
s = 0
for line in lines:
    s += max(line) - min(line)
print(s)

# part 2
s = 0
for line in lines:
    for x in range(len(line) - 1):
        for y in range(x + 1, len(line)):
            if line[x] % line[y] == 0:
                s += line[x] // line[y]
            if line[y] % line[x] == 0:
                s += line[y] // line[x]

print(s)
