numbers = []

with open('in', 'r') as f:
    for line in f.readlines():
        a = int(line)
        numbers.append(a)

N = 25

for i in range(N, len(numbers), 1):
    current = numbers[i]

    # try to find the sum of 2 numbers that matches current in the last N spots
    adds_up = False
    for j in range(i - N, i, 1):
        for k in range(i - N, i, 1):
            # skip adding the same number twice
            if j == k:
                continue

            if numbers[j] + numbers[k] == current:
                adds_up = True
                break
        if adds_up:
            break

    if not adds_up:
        print(current)
        break
