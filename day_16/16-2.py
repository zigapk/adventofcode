import re

input_data = "00111101111101000"
length = 35651584

data = input_data
while len(data) < length:
    a = data
    b = a
    b = b[::-1]
    new_b = ""
    for char in b:
        if char == "1": new_b += "0"
        else: new_b += "1"
    b = new_b
    data = a + "0" + b

data = data[:length]
checksum = data
while checksum == data or len(checksum) % 2 == 0:
    new = ""
    pairs = re.findall('..?', checksum)
    for curr in pairs:
        if curr[0] == curr[1]: new += "1"
        else: new += "0"
    checksum = new

print(checksum)
