with open('in', 'r') as f:
    data = list(map(int, f.readlines()))

for i in data:
    for j in data:
        if i + j == 2020:
            print(i * j)
            exit(0)
