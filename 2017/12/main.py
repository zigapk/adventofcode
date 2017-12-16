import fileinput
from collections import defaultdict
import queue


graph = defaultdict(set)

# generate graph
for line in fileinput.input():
    line = line.split()
    del line[1]

    line = [int(i[:-1]) if ',' in i else int(i) for i in line]

    for i in range(1, len(line), 1):
        graph[line[0]].add(line[i])
        graph[line[i]].add(line[0])

# part 1
seen = set()
q = queue.Queue()
q.put(0)
while not q.empty():
    current = q.get()
    nodes = graph[current]
    for node in nodes:
        if node not in seen:
            seen.add(node)
            q.put(node)

print(len(seen))

# part 2 - could be much faster
groups = set()

for v in graph:
    q = queue.Queue()
    q.put(v)
    seen = set()
    while not q.empty():
        current = q.get()
        nodes = graph[current]
        for node in nodes:
            if node not in seen:
                seen.add(node)
                q.put(node)
    groups.add(str(sorted(list(seen))))

print(len(groups))
