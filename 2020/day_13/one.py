with open('in', 'r') as f:
    start = int(f.readline())
    bus_ids = [int(i) if i != 'x' else None for i in f.readline().strip().split(',')]

minute = start
while True:
    for bus in bus_ids:
        if bus is None:
            continue

        if minute % bus == 0:
            print((minute - start)*bus)
            exit(0)
    minute += 1
