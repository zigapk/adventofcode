import fileinput

jumps = []
jumps2 = []
for line in fileinput.input():
    jumps.append(int(line))
    jumps2.append(int(line))

i = 0
s1 = 0
while i < len(jumps) and i >= 0:
    a = jumps[i]
    jumps[i] += 1
    i += a
    s1 += 1

print(s1)

i = 0
s2 = 0
while i < len(jumps2) and i >= 0:
    a = jumps2[i]
    if a >= 3:
        jumps2[i] -= 1
    else:
        jumps2[i] += 1
    i += a
    s2 += 1
print(s2)
