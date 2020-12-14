from collections import defaultdict
from copy import copy


def print_padded(n):
    print(format(n, '036b'))


def apply_mask_to_address(address, mask):
    address_bin = format(address, '036b')
    new_address_bin = [
        address_bin[i] if mask[i] == '0' else mask[i]
        for i in range(len(address_bin))
    ]
    return ''.join(new_address_bin)


def collapse_address(address):
    result = []
    l = address.count('X')
    n = 2 ** (l)

    for i in range(n):
        bits = '{0:b}'.format(i).zfill(l)
        collapsed_value = list(copy(address))
        for bit in bits:
            collapsed_value[collapsed_value.index('X')] = bit
        result.append(''.join(collapsed_value))

    return result


# mask to be applied
mask_ones = None
mask_zeros = None

# mem
mem = defaultdict(int)

with open('in', 'r') as f:
    for line in f.readlines():
        cmd, _, arg = line.strip().split()

        if cmd == 'mask':
            mask = arg
        else:
            arg = int(arg)
            address = int(cmd.replace('mem[', '').replace(']', ''))
            address = apply_mask_to_address(address, mask)

            for masked_address in collapse_address(address):
                mem[masked_address] = arg

# sum of all the addresses
result = 0
for _, value in mem.items():
    result += value

print(result)
