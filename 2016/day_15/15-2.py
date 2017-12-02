import fileinput

discs = []
for line in fileinput.input():
    line = line[:-2].split()
    discs.append((int(line[3]), int(line[-1])))
discs.append((11, 0))

starttime = 0
while True:
    passed = True
    time = starttime + 1
    for disc in discs:
        if (disc[1] + time) % disc[0] != 0:
            passed = False
            break
        else:
            time += 1
    if passed: break
    starttime += 1

print(starttime)