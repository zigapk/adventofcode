factor_a, factor_b = 16807, 48271
devider = 2147483647

start_a = int(input().split()[-1])
start_b = int(input().split()[-1])

s1 = 0
a = start_a
b = start_b
for i in range(40*10**6):
    a = a*factor_a%devider
    b = b*factor_b%devider

    if i % 10**6 == 0: print(i // 10**6, 'mio done')

    if bin(a)[2:][-16:] == bin(b)[2:][-16:]:
        s1 += 1

print('s1:', s1)

s2 = 0
a = start_a
b = start_b
cmp = []

for i in range(5*10**6):
    if i % 10**6 == 0: print(i // 10**6, 'mio done')
    while True:
        a = (a * factor_a) % devider
        if a % 4 == 0:
            break

    while True:
        b = (b * factor_b) % devider
        if b % 8 == 0:
            break

    if bin(a)[2:][-16:] == bin(b)[2:][-16:]:
        s2 += 1

print('s2:', s2)
