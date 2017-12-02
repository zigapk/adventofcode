import fileinput


def registerInedx(a):
    if a == "a": return 0
    if a == "b": return 1
    if a == "c": return 2
    if a == "d": return 3
    return None


registers = [0 for i in range(4)]
lines = []
for line in fileinput.input():
    line = line[:-1].split()
    lines.append(line)

i = 0
while i < len(lines):
    line = lines[i]
    #print(registers, i, "line: ", " ".join(line))
    if line[0] == "inc":
        registers[registerInedx(line[1])] += 1
    elif line[0] == "dec":
        registers[registerInedx(line[1])] -= 1
    elif line[0] == "jnz":
        try:
            if registers[registerInedx(line[1])] != 0:
                i += int(line[2])
                continue
        except:
            if int(line[1]) != 0:
                i += int(line[2])
                continue
    elif line[0] == "cpy":
        try:
            registers[registerInedx(line[2])] = int(line[1])
        except:
            registers[registerInedx(line[2])] = registers[registerInedx(line[1])]
    i += 1

print(registers[0])