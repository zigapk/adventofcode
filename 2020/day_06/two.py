count = 0
current_group = set()
current_group_len = 0

with open('in', 'r') as f:
    for line in f.readlines():
        l = line.strip()
        current_passenger = set()

        if len(l) == 0:
            # this is end of the last group
            count += len(current_group)
            current_group = set()
            current_group_len = 0
        else:
            # add answers to the current group
            for chr in l:
                current_passenger.add(chr)

            # intersection between current passenger and current group, except for when this is the first passenger in the group
            if current_group_len == 0:
                current_group = current_passenger
            else:
                current_group = current_group.intersection(current_passenger)
            current_group_len += 1

# don't forget the last group
count += len(current_group)

print(count)
