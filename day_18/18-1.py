rows = [".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^."]
goal_size = 40
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

counter = 0
for row in rows:
    print(row)
    for char in row:
        if char == ".": counter += 1
print(counter)
