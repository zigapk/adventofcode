count = 0
current_group = set()

with open('in', 'r') as f:
    for line in f.readlines():
        l = line.strip()

        if len(l) == 0:
            # this is end of the last group
            count += len(current_group)
            current_group = set()
        else:
            # add answers to the current group
            for chr in l:
                current_group.add(chr)

# don't forget the last group
count += len(current_group)

print(count)
