from collections import defaultdict

numbers = []

with open('in', 'r') as f:
    for line in f.readlines():
        numbers.append(int(line.strip()))

numbers.append(0)
numbers.append(max(numbers) + 3)
numbers.sort()

cache = defaultdict(int)


def count_options(index):
    if index in cache:
        return cache[index]

    if index >= len(numbers) - 1:
        return 1

    current = numbers[index]

    options = 0
    for next_index in range(index + 1, len(numbers), 1):
        if numbers[next_index] - current <= 3:
            new_options = count_options(next_index)
            cache[next_index] = new_options
            options += new_options

    return options


print(count_options(0))
