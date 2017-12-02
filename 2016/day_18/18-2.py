rows = [".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^."]
goal_size = 400000
current = 1

while len(rows) < goal_size:
    new_row = ""
    if rows[current - 1][1] == "^": new_row += "^"
    else: new_row += "."

    for i in range(1, len(rows[0])- 1):
        if (rows[current - 1][i - 1] == "^" and rows[current - 1][i] == "^" and rows[current - 1][i + 1] == "." or
                            rows[current - 1][i - 1] == "." and rows[current - 1][i] == "^" and rows[current - 1][
                        i + 1] == "^" or
                            rows[current - 1][i - 1] == "^" and rows[current - 1][i] == "." and rows[current - 1][
                        i + 1] == "." or
                            rows[current - 1][i - 1] == "." and rows[current - 1][i] == "." and rows[current - 1][
                        i + 1] == "^"):
            new_row += "^"
        else: new_row += "."

    if rows[current - 1][-2] == "^": new_row += "^"
    else: new_row += "."
    rows.append(new_row)
    current += 1
    print('\rProgress: [' + '#' * (20 * (current-1) // goal_size) + '-' * (20 - 20 * (current-1) // goal_size) + '] {}% '.format(
        100 * (current-1) // goal_size), end='')

print("\nCounting safe tiles.")
counter = 0
for row in rows:
    for char in row:
        if char == ".": counter += 1
print(counter, "safe tiles found.")
