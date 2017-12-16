import fileinput

firewall = []
current = 0


for line in fileinput.input():
    line = line.split()
    line[0] = str(line[0][:-1])
    line = list(map(int, line))

    if line[0] > current + 1:
        for i in range(line[0]-current-1):
            firewall.append(0)

    firewall.append(line[1])
    current = line[0]


s1 = 0
for i in range(len(firewall)):
    if firewall[i] == 1 or firewall[i] == 2 and i % 2 == 0 or firewall[i] > 2 and i > 0 and i % (2*(firewall[i]-2)+2) == 0:
        s1 += i*firewall[i]

print(s1)

s2 = 1
while True:
    caught = False
    for i in range(len(firewall)):
        if firewall[i] > 0 and (firewall[i] == 1 or (i + s2) % (2 * (firewall[i] - 1)) == 0):
            caught = True
            break

    if not caught:
        break
    s2 += 1
print(s2)
