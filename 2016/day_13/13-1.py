import sys


magic_num = 1364
seen = set()
board = [[0 for i in range(70)] for j in range(70)]


def is_valid(a):
    if a[0] < 0 or a[1] < 0: return False
    if (a[0], a[1]) in seen: return False
    seen.add((a[0], a[1]))
    temp = bin(a[0]**2 + 3*a[0] + 2*a[0]*a[1] + a[1] + a[1]**2 + magic_num).count("1")
    if temp % 2 != 0:
        board[a[0]][a[1]] = 1
        return False
    #print("valid", a[0], a[1])
    if a[0] == 6 and a[1] == 3: board[a[0]][a[1]] = 8
    else: board[a[0]][a[1]] = 0
    return True


def possible_moves(x, y, moves_till_now):
    result = []
    desno = [x+1, y, moves_till_now+1]
    levo = [x-1, y, moves_till_now+1]
    gor = [x, y+1, moves_till_now+1]
    dol = [x, y-1, moves_till_now+1]
    if is_valid(desno): result.append(desno)
    if is_valid(levo): result.append(levo)
    if is_valid(gor): result.append(gor)
    if is_valid(dol): result.append(dol)
    return result


states = possible_moves(0, 0, 0)
#print(states)
depth_counter = 0

while len(states) > 0:
    x, y, moves_till_now = states.pop(0)
    if moves_till_now > depth_counter:
        print("new depth", moves_till_now)
        depth_counter = moves_till_now

    if x == 31 and y == 39:
        print(moves_till_now)
        sys.exit(0)
    else:
        asdf = possible_moves(x, y, moves_till_now)
        states += asdf

for i in range(70):
    for j in range(70):
        print(board[i][j], end="")
    print()