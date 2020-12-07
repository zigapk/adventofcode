from collections import defaultdict

must_contain = defaultdict(list)

with open('in', 'r') as f:
    for line in f.readlines():
        a, b = line.strip().split(' contain ')

        parent = a.replace(' bags', '')
        children = b.split(', ')

        for child in children:
            if 'no other' in child:
                continue
            child_color = ' '.join(child.split()[1:-1])
            child_count = int(child.split()[0])
            must_contain[parent].append((child_count, child_color))


def count_child_bags(color):
    count = 0
    for child in must_contain[color]:
        child_count, child_color = child
        each_contains = count_child_bags(child_color)
        count += child_count * (each_contains + 1)
    return count


print(count_child_bags('shiny gold'))
