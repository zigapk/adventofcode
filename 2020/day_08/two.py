instructions = []

with open('in', 'r') as f:
    for line in f.readlines():
        instruction, arg = line.split()
        arg = int(arg)
        instructions.append((instruction, arg))


def is_loop(instructions):
    seen_program_counters = set()
    acc = 0
    pc = 0

    while pc < len(instructions):
        if pc in seen_program_counters:
            # this is a loop
            return True, acc

        seen_program_counters.add(pc)

        instruction, arg = instructions[pc]

        if instruction == 'nop':
            pc += 1
        elif instruction == 'acc':
            acc += arg
            pc += 1
        elif instruction == 'jmp':
            pc += arg

    # this is not a loop
    return False, acc


def modify_instructions(original, i):
    modified = []
    for j in range(len(original)):
        if i == j:
            instruction, arg = original[i]
            if instruction == 'acc':
                return None

            if instruction == 'jmp':
                modified.append(('nop', arg))
            else:
                modified.append(('jmp', arg))
        else:
            modified.append(original[j])
    return modified


# attempt to modify each instruction
for i in range(len(instructions)):
    modified = modify_instructions(instructions, i)

    if modified is None:
        continue

    loop, acc = is_loop(modified)

    if not loop:
        print(acc)
        break
