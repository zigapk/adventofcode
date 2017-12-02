result = ""
digits = [[-1, -1, 1, -1, -1],
          [-1, 2, 3, 4, -1],
          [5, 6, 7, 8, 9],
          [-1, 10, 11, 12, -1],
          [-1, -1, 13, -1, -1]]
index = (2, 0)

for i in range(5):
    for char in input():
        if char == "U" and index[0] != 0 and digits[index[0]-1][index[1]] != -1:
            index = (index[0] - 1, index[1])
        elif char == "D" and index[0] != 4 and digits[index[0]+1][index[1]] != -1:
            index = (index[0] + 1, index[1])
        elif char == "R" and index[1] != 4 and digits[index[0]][index[1] + 1] != -1:
            index = (index[0], index[1] + 1)
        elif char == "L" and index[1] != 0 and digits[index[0]][index[1] - 1] != -1:
            index = (index[0], index[1] - 1)
    result += hex(digits[index[0]][index[1]])[2:].upper()
print(result)
