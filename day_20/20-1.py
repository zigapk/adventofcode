import fileinput

ranges = []
for line in fileinput.input():
    line = line[:-1].split("-")
    ranges.append(sorted([int(line[0]), int(line[1])]))
ranges.sort()

i = 0
while i <= 4294967295:
    dela = True
    for j in range(len(ranges)):
        if ranges[j][0] <= i <= ranges[j][1]:
            i = ranges[j][1]
            ranges.pop(j)
            dela = False
            break
    if dela:
        print(i)
        break
    i += 1
