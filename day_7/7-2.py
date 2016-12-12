import fileinput

def is_aba(a):
    if len(a) == 3 and a[0] == a[2] and a[0] != a[1]: return True
    return False

def bab_from_aba(a):
    return "".join([a[1], a[0], a[1]])

def devide_into_in_and_out(a):
    inside_list = []
    outside_list = []
    current = ""
    for char in a:
        if char == "[":
            outside_list.append(current)
            current = ""
        elif char == "]":
            inside_list.append(current)
            current = ""
        else:
            current += char
    outside_list.append(current)

    return (outside_list, inside_list)

counter = 0
for line in fileinput.input():
    line = line[:-1]
    outside, inside = devide_into_in_and_out(line)
    aba = []
    for item in outside:
        for i in range(len(item)-2):
            if is_aba(item[i:i+3]): aba.append(item[i:i+3])
    is_ssl = False
    for item in inside:
        for aba_sequence in aba:
            reverse = bab_from_aba(aba_sequence)
            for i in range(len(item)-2):
                if item[i:i+3] == reverse: is_ssl = True
    if is_ssl: counter += 1
print(counter)

