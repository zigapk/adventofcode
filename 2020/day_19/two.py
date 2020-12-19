rules = {}

lines = [l.strip() for l in open('in', 'r').readlines()]

rule_lines = lines[:lines.index('')]
message_lines = lines[lines.index('') + 1:]

for line in rule_lines:
    rule_id, rule = line.split(':')
    rule = rule.strip()
    rules[rule_id] = rule

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'


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


# intersection of options_31 and option_42 is empty
options_31 = generate_options(rules['31'])
options_42 = generate_options(rules['42'])

L = len(options_31[0])
count = 0

for message in message_lines:
    l = len(message)

    if l % L != 0:
        continue

    if l / 3 < 3:
        continue

    # try to match 42 as far as we can
    i = 0
    count_42 = 0
    while i < l:
        s = message[i:i + L]
        if s not in options_42:
            break
        else:
            count_42 += 1

        i += L

    if i == 0 or i >= l - 1:
        continue

    matches = True
    count_31 = 0
    for j in range(i, l, L):
        s = message[j:j + L]
        if s not in options_31:
            matches = False
            break
        else:
            count_31 += 1

    if not matches:
        continue

    if count_31 >= count_42:
        continue

    # print(message)
    count += 1

print(count)
