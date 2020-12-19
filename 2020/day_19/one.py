rules = {}

lines = [l.strip() for l in open('in', 'r').readlines()]

rule_lines = lines[:lines.index('')]
message_lines = lines[lines.index('') + 1:]

for line in rule_lines:
    rule_id, rule = line.split(':')
    rule = rule.strip()
    rules[rule_id] = rule


def generate_options(rule):
    if '"' in rule:
        return [rule.replace('"', '')]

    if '|' in rule:
        parts = [part.strip() for part in rule.split('|')]
        res = []
        for part in parts:
            res += generate_options(part)
        return res

    subrules = rule.split()
    res = []
    for i in range(len(subrules)):
        current = subrules[i]

        if i == 0:
            res = generate_options(rules[current])
        else:
            new_res = []
            cross = generate_options(rules[current])
            for a in res:
                for b in cross:
                    new_res.append(a + b)

            res = new_res
    return res


options = generate_options(rules['0'])

count = 0
for message in message_lines:
    if message in options:
        count += 1
print(count)
