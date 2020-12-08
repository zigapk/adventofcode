instructions = []

with open('in', 'r') as f:
    for line in f.readlines():
        instruction, arg = line.split()
        arg = int(arg)
        instructions.append((instruction, arg))

seen_program_counters = set()
acc = 0
pc = 0

while pc < len(instructions):
    if pc in seen_program_counters:
        break

    seen_program_counters.add(pc)

    instruction, arg = instructions[pc]

    if instruction == 'nop':
        pc += 1
    elif instruction == 'acc':
        acc += arg
        pc += 1
    elif instruction == 'jmp':
        pc += arg
print(acc)
