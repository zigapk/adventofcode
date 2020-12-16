with open('in', 'r') as f:
    lines = [i.strip() for i in f]
    rules_lines, lines = lines[:lines.index('')], lines[lines.index('') + 1:]
    my_ticket_lines, nearby_tickets_lines = lines[:lines.index('')], lines[lines.index('') + 2:]

all_valid_numbers = set()
rules = {}
rule_names = []

for rule_line in rules_lines:
    rule_name, rules_str = rule_line.split(':')
    rule_names.append(rule_name)

    valid_numbers = set()
    for rule in rules_str.split('or'):
        r = rule.strip().split('-')
        a, b = int(r[0].strip()), int(r[1].strip())
        for i in range(a, b + 1):
            valid_numbers.add(i)
            all_valid_numbers.add(i)

    rules[rule_name] = valid_numbers

tickets = []
for ticket_line in nearby_tickets_lines:
    tickets.append(list(map(int, ticket_line.split(','))))

my_ticket = list(map(int, my_ticket_lines[1].split(',')))
tickets.append(my_ticket)
possible_positions = [set(rule_names) for _ in range(len(my_ticket))]

for ticket in tickets:
    for rule_i in range(len(rule_names)):
        for num_i in range(len(rule_names)):
            rule_name = rule_names[rule_i]
            current_number = ticket[num_i]

            if current_number not in all_valid_numbers:
                continue

            if current_number not in rules[rule_name]:
                if rule_name in possible_positions[num_i]:
                    possible_positions[num_i].remove(rule_name)

while sum([len(i) for i in possible_positions]) != len(rule_names):
    for i in range(len(possible_positions)):
        if len(possible_positions[i]) == 1:
            for j in range(len(possible_positions)):
                if i == j:
                    continue

                # get element without removal
                rule_name = None
                for el in possible_positions[i]:
                    rule_name = el
                    break

                if rule_name in possible_positions[j]:
                    possible_positions[j].remove(rule_name)

result = 1
for i in range(len(possible_positions)):
    rule_name = possible_positions[i].pop()
    if not rule_name.startswith('departure'):
        continue

    result *= my_ticket[i]

print(result)
