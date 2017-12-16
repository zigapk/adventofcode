from collections import defaultdict
import fileinput

mem = defaultdict(int)
s1 = -100000
s2 = -100000

def condition(line):
    global mem
    l = line[-3:]

    if l[1] == "==":
        if mem[l[0]] == int(l[2]): return True
        else: return False
    elif l[1] == "<":
        if mem[l[0]] < int(l[2]): return True
        else: return False
    elif l[1] == ">":
        if mem[l[0]] > int(l[2]): return True
        else: return False
    elif l[1] == "<=":
        if mem[l[0]] <= int(l[2]): return True
        else: return False
    elif l[1] == ">=":
        if mem[l[0]] >= int(l[2]): return True
        else: return False
    elif l[1] == "!=":
        if mem[l[0]] != int(l[2]): return True
        else: return False


for line in fileinput.input():
    line = line.split()
    if condition(line):
        if line[1] == "inc":
            mem[line[0]] += int(line[2])
        elif line[1] == "dec":
            mem[line[0]] -= int(line[2])
        if mem[line[0]] > s2: s2 = mem[line[0]]


for k in mem.keys():
    if mem[k] > s1: s1 = mem[k]
print(s1)
print(s2)
