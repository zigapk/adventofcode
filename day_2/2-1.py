result = ""
digits = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = (1, 1)

for i in range(5):
    for char in input():
        if char == "U" and index[0] != 0:
            index = (index[0] - 1, index[1])
        elif char == "D" and index[0] != 2:
            index = (index[0] + 1, index[1])
        elif char == "R" and index[1] != 2:
            index = (index[0], index[1] + 1)
        elif char == "L" and index[1] != 0:
            index = (index[0], index[1] - 1)
    result += str(digits[index[0]][index[1]])
print(result)
