from collections import deque

q1 = deque()
q2 = deque()

player_2 = False
with open('in', 'r') as f:
    f.readline()

    for line in f.readlines():
        try:
            i = int(line.strip())
            if player_2:
                q2.append(i)
            else:
                q1.append(i)
        except Exception:
            player_2 = True

while len(q1) > 0 and len(q2) > 0:
    card1 = q1.popleft()
    card2 = q2.popleft()
    if card1 > card2:
        q1.append(max(card1, card2))
        q1.append(min(card1, card2))
    else:
        q2.append(max(card1, card2))
        q2.append(min(card1, card2))

q = q1 if len(q2) == 0 else q2
result = 0
for i in range(1, len(q) + 1):
    result += i * q.pop()

print(result)
