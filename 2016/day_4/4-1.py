import fileinput
import string
import operator

def checksum(a):
    count = {}
    for char in string.ascii_lowercase:
        count[char] = a.count(char)
    sorted_count = sorted(count.items(), key=operator.itemgetter(1))
    last_number = sorted_count[0][1]
    current_sequence = ""
    result = ""

    for item in sorted_count[::-1]:
        if item[1] == 0:
            result += "".join(sorted(current_sequence))
            break
        elif item[1] == last_number:
            current_sequence += item[0]
        else:
            result += "".join(sorted(current_sequence))
            current_sequence = item[0]
            last_number = item[1]
    return result[:5]


sum = 0
for line in fileinput.input():
    *name, other = line.split("-")
    name = "".join(name).replace("-", "")
    sector_id, original_checksum = int(other[0:other.index("[")]), other[other.index("[")+1:-2]
    if checksum(name) == original_checksum:
        sum += sector_id
print(sum)
