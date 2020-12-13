with open('in', 'r') as f:
    f.readline()
    bus_ids = [int(i) if i != 'x' else None for i in f.readline().strip().split(',')]

# id -> number of minutes after t it arrives
factors = {}
for i in range(len(bus_ids)):
    if bus_ids[i] is None:
        continue
    factors[bus_ids[i]] = i

# lowest common multiple
lcm = 1
for bus_id in factors.keys():
    lcm *= bus_id

start_time = 0
for bus_id in factors.keys():
    offset = factors[bus_id]
    start_time += int(lcm / bus_id) * pow(int(lcm / bus_id), -1, bus_id) * offset

print(lcm - (start_time % lcm))
