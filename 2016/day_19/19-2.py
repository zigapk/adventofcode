arr = [i+1 for i in range(3018458)]


def index_from_len(i, n):
    return (n // 2 + i) % n

i = 0
counter = 0
while len(arr) > 1:
    if counter % 1000 == 0: print(len(arr))
    to_pop = index_from_len(i, len(arr))
    del arr[to_pop]
    if to_pop < i: i = i % len(arr)
    else: i = (i+1) % len(arr)
    counter += 1
print(arr[0])
