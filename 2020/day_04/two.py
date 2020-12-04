passports = []

current = {}
with open('in', 'r') as f:
    for line in f.readlines():

        # end of passport, save and prepare for the next one
        if line == '\n':
            passports.append(current)
            current = {}

        # process single line
        raw_data = line.split()
        for item in raw_data:
            k, v = item.split(':')
            current[k] = v

# don't forget the last one
passports.append(current)

# check validity
count = 0
for passport in passports:

    # check byr
    if 'byr' not in passport:
        continue
    byr = passport['byr']
    if int(byr) > 2002 or int(byr) < 1920:
        continue

    # check iyr
    if 'iyr' not in passport:
        continue
    iyr = passport['iyr']
    if int(iyr) > 2020 or int(iyr) < 2010:
        continue

    # check eyr
    if 'eyr' not in passport:
        continue
    eyr = passport['eyr']
    if int(eyr) > 2030 or int(eyr) < 2020:
        continue

    # check hgt
    if 'hgt' not in passport:
        continue
    hgt = passport['hgt']
    if not hgt.endswith('cm') and not hgt.endswith('in'):
        continue
    if hgt.endswith('cm'):
        h = int(hgt[:-2])
        if h < 150 or h > 193:
            continue
    if hgt.endswith('in'):
        h = int(hgt[:-2])
        if h < 59 or h > 76:
            continue

    # check hcl
    if 'hcl' not in passport:
        continue
    hcl = passport['hcl']
    if hcl[0] != '#' or len(hcl) != 7:
        continue
    hcl_valid = True
    for c in hcl[1:]:
        if c not in 'abcdef0123456789':
            hcl_valid = False
            break
    if not hcl_valid:
        continue

    # check ecl
    if 'ecl' not in passport:
        continue
    ecl = passport['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

    # check pid
    if 'pid' not in passport:
        continue
    pid = passport['pid']
    if len(pid) != 9:
        continue

    count += 1

print(count)
