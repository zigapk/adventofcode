valid_numbers = set()

with open('in', 'r') as f:
    lines = [i.strip() for i in f]
    rules_lines, lines = lines[:lines.index('')], lines[lines.index('') + 1:]
    my_ticket_lines, nearby_tickets_lines = lines[:lines.index('')], lines[lines.index('') + 2:]

for rule_line in rules_lines:
    line = rule_line.split(':')[1].split()

    for item in line:
        if item == 'or':
            continue
        a, b = item.split('-')
        a, b = int(a), int(b)

        for i in range(a, b + 1):
            valid_numbers.add(i)

result = 0
for ticket_line in nearby_tickets_lines:
    numbers = map(int, ticket_line.split(','))
    for n in numbers:
        if n not in valid_numbers:
            result += n

print(result)
