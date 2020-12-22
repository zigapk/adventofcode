from copy import deepcopy

d1 = []
d2 = []

player_2 = False
with open('in', 'r') as f:
    f.readline()

    for line in f.readlines():
        try:
            i = int(line.strip())
            if player_2:
                d2.append(i)
            else:
                d1.append(i)
        except Exception:
            player_2 = True

seen = set()

next_game_id = 1

last_deck_1 = None
last_deck_2 = None


def game(deck1, deck2, game_id=0):
    global next_game_id, last_deck_1, last_deck_2

    while len(deck1) > 0 and len(deck2) > 0:
        h = (str(game_id), str(deck1), str(deck2))
        if h in seen:
            return 1

        seen.add(h)

        card1, deck1 = deck1[0], deck1[1:]
        card2, deck2 = deck2[0], deck2[1:]

        if len(deck1) >= card1 and len(deck2) >= card2:
            next_game_id += 1
            player_1_wins = game(deepcopy(deck1[:card1]), deepcopy(deck2[:card2]), game_id=next_game_id - 1) == 1
        else:
            player_1_wins = card1 > card2

        if player_1_wins:
            deck1 = deepcopy(deck1) + [card1, card2]
        else:
            deck2 = deepcopy(deck2) + [card2, card1]

    last_deck_1 = deck1
    last_deck_2 = deck2
    return 1 if len(deck2) == 0 else 2


game(deepcopy(d1), deepcopy(d2))

res = 0
d = last_deck_1 if len(last_deck_2) == 0 else last_deck_2
d = list(reversed(d))
for i in range(1, len(d) + 1):
    res += i * d[i - 1]

print(res)
