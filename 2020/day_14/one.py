from collections import defaultdict

# mask to be applied
mask_ones = None
mask_zeros = None

# mem
mem = defaultdict(int)

with open('in', 'r') as f:
    for line in f.readlines():
        cmd, _, arg = line.strip().split()

        if cmd == 'mask':
            mask_ones = int(arg.replace('X', '0'), 2)
            mask_zeros = int(arg.replace('X', '1'), 2)
        else:
            arg = int(arg)
            address = cmd.replace('mem[', '').replace(']', '')

            # apply mask to the arg
            to_write = (arg | mask_ones) & mask_zeros
            mem[address] = to_write

# sum of all the addresses
result = 0
for _, value in mem.items():
    result += value

print(result)
