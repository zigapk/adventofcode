def dolzina(string):
    asdf = True
    inside = False
    ena = ""
    dva = ""
    length = 0
    i = -1
    while len(string) > i:
        i += 1
        char = string[i]
        if char == "(":
            inside = True
            continue
        if char == ")":
            inside = False
            asdf = True
            print(ena, dva)
            length += int(dva) * dolzina(string[i: i + int(ena)])
            i += int(ena)
            ena = ""
            dva = ""
            continue
        if inside:
            if char == "x":
                asdf = False
                continue
            if asdf: ena += char
            else: dva += char
        else: length += 1
    return length

print(dolzina(input()))