import fileinput

bots = [{"chips": [], "low": -1, "high": -1, "lowout": False, "highout": False} for i in range(210)]

for line in fileinput.input():
    line = line[:-1]
    line = line.split()
    if line[0] == "value":
        bots[int(line[-1])]["chips"].append(int(line[1]))
    elif line[0] == "bot":
        bots[int(line[1])]["low"] = int(line[6])
        if line[5] == "output": bots[int(line[1])]["lowout"] = True
        bots[int(line[1])]["high"] = int(line[-1])
        if line[-2] == "output": bots[int(line[1])]["highout"] = True

found = False
while found == False:
    for bot in bots:
        if len(bot["chips"]) == 2:
            chips = sorted(bot["chips"])
            if chips[0] == 17 and chips[1] == 61:
                print(bots.index(bot))
                found = True
                break
            else:
                if not bot["lowout"]: bots[bot["low"]]["chips"].append(chips[0])
                if not bot["highout"]: bots[bot["high"]]["chips"].append(chips[1])
                bot["chips"] = []
