import fileinput

result = ""
file = input()

i = 0
while i < len(file):
    if file[i] == "(":
        closing = file.index(")", i)
        length, times = [int(a) for a in file[i+1:closing].split("x")]
        i = closing + 1
        sequence = file[i:i+length]
        result += times*sequence
        i += length
    else:
        result += file[i]
        i += 1

print(len(result))
