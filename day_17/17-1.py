import hashlib

salt = "gdjjyniy"

def possible_moves(state):
    result = []
    hash = hashlib.md5((salt + state[2]).encode('utf-8')).hexdigest()
    if state[1] > 0 and hash[0] in "bcdef":
        result.append((state[0], state[1]-1, state[2]+"U"))
    if state[1] < 3 and hash[1] in "bcdef":
        result.append((state[0], state[1]+1, state[2]+"D"))
    if state[0] > 0 and hash[2] in "bcdef":
        result.append((state[0]-1, state[1], state[2]+"L"))
    if state[0] < 3 and hash[3] in "bcdef":
        result.append((state[0]+1, state[1], state[2]+"R"))
    return result


initial_state = (0, 0, "")
moves = possible_moves(initial_state)

while len(moves) > 0:
    state = moves.pop(0)
    if state[0] == 3 and state[1] == 3:
        print(state[2])
        break
    else:
        moves += possible_moves(state)