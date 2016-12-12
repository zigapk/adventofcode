import fileinput

def shift(l, n):
    return l[-n:] + l[:-n]

screen = [[0 for j in range(50)] for i in range(6)]

for line in fileinput.input():
    line = line[:-1].split()
    if line[0] == "rect":
        x, y = [int(a) for a in line[1].split("x")]
        for i in range(x):
            for j in range(y):
                screen[j][i] = 1
    elif line[0] == "rotate":
        if line[1] == "row":
            row = int(line[2][line[2].index("=")+1:])
            by = int(line[4])
            screen[row] = shift(screen[row], by)
        elif line[1] == "column":
            column = int(line[2][line[2].index("=") + 1:])
            by = int(line[4])
            to_shift = [screen[i][column] for i in range(6)]
            shifted = shift(to_shift, by)
            for i in range(6):
                screen[i][column] = shifted[i]

counter = 0
for j in range(6):
    for i in range(50):
        if screen[j][i] == 1:
            counter += 1
            print(u"\u2588", end="")
        else: print(" ", end="")
    print()
print(counter)

