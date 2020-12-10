numbers = []

with open('in', 'r') as f:
    for line in f.readlines():
        numbers.append(int(line.strip()))

numbers.append(0)
numbers.append(max(numbers) + 3)
numbers.sort()

ones = sum([numbers[i + 1] - numbers[i] == 1 for i in range(len(numbers) - 1)])
threes = sum([numbers[i + 1] - numbers[i] == 3 for i in range(len(numbers) - 1)])

print(ones*threes)
