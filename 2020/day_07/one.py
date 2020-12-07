from collections import defaultdict

can_be_contained_in = defaultdict(set)

with open('in', 'r') as f:
    for line in f.readlines():
        a, b = line.strip().split(' contain ')

        parent = a.replace(' bags', '')
        children = b.split(', ')

        for child in children:
            child_color = ' '.join(child.split()[1:-1])
            can_be_contained_in[child_color].add(parent)

seen_colors = set()


def count_possible_parent_colors(color):
    for parent_color in can_be_contained_in[color]:
        seen_colors.add(parent_color)
        count_possible_parent_colors(parent_color)


count_possible_parent_colors('shiny gold')
print(len(seen_colors))
