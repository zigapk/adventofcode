max_id = -1

with open('in', 'r') as f:
    for line in f.readlines():
        # extract string parts
        row_s = line[:7]
        col_s = line[7:10]

        # replace with 0 and 1
        row_s = row_s.replace('B', '1').replace('F', '0')
        col_s = col_s.replace('R', '1').replace('L', '0')

        # convert to ints and then id
        row = int(row_s, 2)
        col = int(col_s, 2)
        i = row * 8 + col

        # remember the biggest one
        if i > max_id:
            max_id = i

print(max_id)
