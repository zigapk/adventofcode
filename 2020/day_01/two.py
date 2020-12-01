with open('in', 'r') as f:
    data = list(map(int, f.readlines()))

for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i * j * k)
                exit(0)
