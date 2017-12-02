arr = [i + 1 for i in range(3018458)]

liho = len(arr) % 2
arr = arr[::2]
while len(arr) > 1:
    new_liho = len(arr) % 2 != liho
    if liho:
        arr = arr[1::2]
    else:
        arr = arr[::2]
    liho = new_liho

print(arr[0])
