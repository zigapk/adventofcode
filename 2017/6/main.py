import copy

banks = list(map(int, input().split()))

def solve(banks2):
    banks = copy.deepcopy(banks2)
    seen = set()
    s = 0
    while str(banks) not in seen:
        seen.add(str(banks))
        index =  banks.index(max(banks))
        orig_index = index
        a = banks[index]
        banks[index] = 0
        index += 1
        while a > 0:
            banks[index % (len(banks))] += 1
            a -= 1
            index += 1
        s += 1
    return s, banks

s1, banks = solve(banks)
print(s1)
s2, _ = solve(banks)
print(s2)
