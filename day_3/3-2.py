import fileinput

counter = 0
triangles = []
templines = []

for line in fileinput.input():
    templines.append([int(a) for a in line.split()])
    if len(templines) == 3:
        for asdf in range(3):
            triangles.append((templines[0][asdf], templines[1][asdf], templines[2][asdf]))
        templines = []

for sides in triangles:
    sides = sorted(sides)
    if sides[0] + sides[1] > sides[2]:
        counter += 1

print(counter)
