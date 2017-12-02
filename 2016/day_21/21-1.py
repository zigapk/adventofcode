import fileinput

password = "abcdefgh"

for line in fileinput.input():
    line = line[:-1].split()
    if line[0] == "swap":
        if line[1] == "position":
            ena = int(line[2])
            dva = int(line[-1])
            new = list(password)
            new[ena] = password[dva]
            new[dva] = password[ena]
            password = "".join(new)
        elif line[1] == "letter":
            new = ""
            for char in password:
                if char == line[2]: new += line[-1]
                elif char == line[-1]: new += line[2]
                else: new += char
            password = new
    elif line[0] == "rotate":
        if line[1] == "right":
            for i in range(int(line[-2])):
                old = password[-1]
                password = password[:-1]
                password = old + password
        elif line[1] == "left":
            for i in range(int(line[-2])):
                old = password[0]
                password = password[1:]
                password += old
        elif line[1] == "based":
            i = 1
            if password.index(line[-1]) >= 4: i += 1
            for i in range(password.index(line[-1])+i):
                old = password[-1]
                password = password[:-1]
                password = old + password
    elif line[0] == "reverse":
        x = int(line[-3])
        y = int(line[-1])
        password = password[:x] + password[x:y+1][::-1] + password[y+1:]
    elif line[0] == "move":
        password = list(password)
        old = password.pop(int(line[2]))
        password.insert(int(line[-1]), old)
        password = "".join(password)

print(password)

