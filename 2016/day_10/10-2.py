import fileinput

bots = [{"chips": [], "low": -1, "high": -1, "lowout": -1, "highout": -1} for i in range(210)]
outputs = [[] for i in range(21)]

for line in fileinput.input():
    line = line[:-1]
    line = line.split()
    if line[0] == "value":
        bots[int(line[-1])]["chips"].append(int(line[1]))
    elif line[0] == "bot":
        if line[5] == "output":
            bots[int(line[1])]["low"] = -1
            bots[int(line[1])]["lowout"] = int(line[6])
        else:
            bots[int(line[1])]["low"] = int(line[6])
            bots[int(line[1])]["lowout"] = -1
        if line[-2] == "output":
            bots[int(line[1])]["high"] = -1
            bots[int(line[1])]["highout"] = int(line[-1])
        else:
            bots[int(line[1])]["high"] = int(line[-1])
            bots[int(line[1])]["highout"] = -1

did_something = True
while did_something:
    did_something = False
    for bot in bots:
        if len(bot["chips"]) == 2:
            did_something = True
            chips = sorted(bot["chips"])
            if bot["lowout"] != -1: outputs[bot["lowout"]].append(chips[0])
            else: bots[bot["low"]]["chips"].append(chips[0])
            if bot["highout"] != -1: outputs[bot["highout"]].append(chips[1])
            else: bots[bot["high"]]["chips"].append(chips[1])
            bot["chips"] = []

print(outputs[0])
print(outputs[1])
print(outputs[2])
print("multiplied:", str(outputs[0][0]*outputs[1][0]*outputs[2][0]))
