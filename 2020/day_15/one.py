spoken_numbers = {}

with open('in', 'r') as f:
    numbers = f.readline().split(',')

for i in range(len(numbers)):
    last_number = int(numbers[i])

    if last_number not in spoken_numbers:
        spoken_numbers[last_number] = [i]
    else:
        spoken_numbers[last_number] = [i, spoken_numbers[last_number][0]]

total_spoken = len(numbers)

for i in range(total_spoken, 2020):
    if len(spoken_numbers[last_number]) == 1:
        last_number = 0
    else:
        last_number = spoken_numbers[last_number][0] - spoken_numbers[last_number][1]

    if last_number in spoken_numbers:
        spoken_numbers[last_number] = [i, spoken_numbers[last_number][0]]
    else:
        spoken_numbers[last_number] = [i]

print(last_number)
