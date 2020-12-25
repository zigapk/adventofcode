N = 20201227

with open('in', 'r') as f:
    public_key_card = int(f.readline().strip())
    public_key_door = int(f.readline().strip())


def guess_loop_size(public_key):
    loop_size = 0
    current = 1
    while current != public_key:
        current *= 7
        current %= N
        loop_size += 1
    return loop_size


def transform(loop_size, subject):
    current = 1
    for _ in range(loop_size):
        current *= subject
        current %= N
    return current


loop_size_card = guess_loop_size(public_key_card)
loop_size_door = guess_loop_size(public_key_door)

print(transform(loop_size_door, public_key_card))
