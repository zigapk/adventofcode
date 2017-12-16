import fileinput

class Node():
    def __init__(self, name, children):
        self.name = name
        self.children = children
    def getname(self):
        return self.name
    def getchildren(self):
        return self.children

structure = []
weights = {}
answers = []

def weightsum(node):
    r = weights[node.name]
    for c in node.children:
        r += weightsum(c)
    return r


def fill(root, structure):
    for el in structure:
        if el[0] == root.getname():
            root.children.append(Node(el[1], []))
    for i in range(len(root.children)):
        root.children[i] = fill(root.children[i], structure)
    return root

def find(node):
    if len(node.children) > 0:
        teze = [weightsum(i) for i in node.children]
        if max(teze) != min(teze):
            diff = max(teze) - min(teze)
            i = teze.index(max(teze))
            answers.append(weights[node.children[i].name] - diff)

        for c in node.children:
            find(c)


for line in fileinput.input():
    line = line.split()
    name = line[0]
    weight = int(line[1][1:-1])
    weights[name] = weight

    if len(line) > 3:
        children = line[3:]
        for c in children:
            if c[-1] == ',': c = c[:-1]
            structure.append((name, c))

top = structure[0][0]
i = 0
while i < len(structure):
    if structure[i][1] == top:
        top = structure[i][0]
        i = 0
    i += 1

# make a tree
root = Node(top, [])
fill(root, structure)

print(top)

# weights['inwmb'] = 53037
# weights['ugml'] = 60
find(root)
print(answers[-1])
