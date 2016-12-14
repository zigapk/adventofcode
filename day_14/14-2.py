import hashlib


def md5x2016(a):
    result = hashlib.md5(a.encode('utf-8')).hexdigest()
    for i in range(2016): result = hashlib.md5(result.encode('utf-8')).hexdigest()
    return result


def has_n_sequence(a, n):
    for i in range(len(a) - n +1):
        if a[i:i + n] == n * a[i]: return True, a[i]
    return False, ""


index = 0
salt = "ahsbgdzn"
valid = []
active = []

while len(valid) <= 64:
    hash = md5x2016(salt + str(index))
    has3, char3 = has_n_sequence(hash, 3)
    if has3:
        active.append((index, hash, char3))

    has_5, _ = has_n_sequence(hash, 5)

    if has_5:
        new_active = []
        for j in range(len(active)):
            if active[j][0] + 1000 >= index:
                if active[j][0] == index:
                    new_active.append(active[j])
                elif 5*active[j][2] in hash:
                    valid.append(active[j])
                else: new_active.append(active[j])
        active = new_active
    index += 1

valid.sort()
print(valid[63][0])