import fileinput

counter = 0

for line in fileinput.input():
    sides = sorted([int(a) for a in line.split()])
    if sides[0] + sides[1] > sides[2]:
        counter += 1
print(counter)
