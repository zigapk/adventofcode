import fileinput

counter = [{}, {}, {}, {}, {}, {}, {}, {}]
for line in fileinput.input():
    line = line[:-1]
    for i in range(len(line)):
        try:
            counter[i][line[i]] += 1
        except:
            counter[i][line[i]] = 1

result = ""
for position in counter:
    biggest = ""
    count_biggest = -1
    for key, value in position.items():
        if value < count_biggest or count_biggest == -1:
            count_biggest = value
            biggest = key
    result += biggest

print(result)
