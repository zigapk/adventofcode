

def isCharValid(line, i):
    if i == 0: return True
    if line[i-1] != "!": return True
    return(not isCharValid(line, i-1))

line = input()

s1, s2 = 0, 0
score = 0
garbage = False
for i in range((len(line))):
    if isCharValid(line, i):
        if garbage and line[i] not in '!>': s2 += 1

        if line[i] == "{" and not garbage:
            score += 1
            s1 += score
        elif line[i] == "}" and not garbage:
            score -= 1
        elif line[i] == "<" and not garbage:
            garbage = True
        elif line[i] == ">":
            garbage = False
print(s1)
print(s2)
