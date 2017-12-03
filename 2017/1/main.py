import fileinput

s1, s2 = 0, 0
for line in fileinput.input():
    for i in range(len(line)):
        if line[i] == line[(i+1) % (len(line) -1)]:
            s1 += int(line[i])
        if line[i] == line[(i+len(line)//2) % (len(line) - 1)]:
            s2 += int(line[i])

print(s1)
print(s2)
