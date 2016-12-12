import fileinput
import string
import operator


def checksum(a):
    a = "".join(a).replace("-", "")
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


def caesar(ciphertext, n):
    result = ''
    key = string.ascii_lowercase
    for l in ciphertext:
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


real_rooms = []

sum = 0
for line in fileinput.input():
    *name, other = line.split("-")
    name = "-".join(name)
    sector_id, original_checksum = int(other[0:other.index("[")]), other[other.index("[") + 1:-2]
    if checksum(name) == original_checksum:
        real_rooms.append((name, sector_id))

for room in real_rooms:
    if "north" in caesar(room[0], room[1]):
        print(room, caesar(room[0], room[1]), room[1])