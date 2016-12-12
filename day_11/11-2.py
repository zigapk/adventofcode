import copy
import sys

def is_valid(state, elevator):
    if elevator < 0 or elevator > 3: return False
    if (elevator, str(state)) in seen:
        return False
    else:
        seen.add((elevator, str(state)))
        no_pair_chip = []
        for pair in state:
            if pair[0] == pair[1]: continue
            no_pair_chip.append(pair[0])

        for pair in state:
            if pair[1] in no_pair_chip:
                return False
        return True


def valid_states(elevator, moves_till_now, state):
    result = []
    for i in range(len(state)):
        for j in range(2):
            if state[i][j] == elevator:
                up = copy.deepcopy(state)
                up[i][j] += 1
                up.sort()
                down = copy.deepcopy(state)
                down[i][j] -= 1
                down.sort()
                if is_valid(up, elevator + 1): result.append((elevator + 1, moves_till_now + 1, up))
                if is_valid(down, elevator - 1): result.append((elevator - 1, moves_till_now + 1, down))
    for i in range(len(state)):
        for k1 in range(2):
            for j in range(i, len(state)):
                for k2 in range(2):
                    if i == j and k1 == k2: continue
                    if state[i][k1] == elevator and state[j][k2] == elevator:
                        up = copy.deepcopy(state)
                        up[i][k1] += 1
                        up[j][k2] += 1
                        up.sort()
                        if is_valid(up, elevator + 1): result.append((elevator + 1, moves_till_now + 1, up))
                        down = copy.deepcopy(state)
                        down[i][k1] -= 1
                        down[j][k2] -= 1
                        down.sort()
                        if is_valid(down, elevator - 1): result.append((elevator - 1, moves_till_now + 1, down))
    return result


def is_result(state):
    for st in state:
        if st[0] != 3 or st[1] != 3: return False
    return True


state = [[0, 0], [0, 0], [0, 0], [2, 1], [2, 1], [2, 1], [2, 1]]  # generators by pairs
state.sort()
seen = set()
elevator = 0

states = valid_states(elevator, 0, state)  # (elevator, moves till now, state)
previous_depth = 0

while len(states) > 0:
    elevator, moves_till_now, state = states.pop(0)  # pop front
    if moves_till_now > previous_depth:
        print("entered new depth:", moves_till_now)
        previous_depth = moves_till_now

    if is_result(state):
        print(moves_till_now)
        sys.exit(0)
    else:
        valid_moves = valid_states(elevator, moves_till_now, state)
        states += valid_moves
