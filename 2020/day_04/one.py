REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
]

passports = []

current = []
with open('in', 'r') as f:
    for line in f.readlines():

        # end of passport, save and prepare for the next one
        if line == '\n':
            passports.append(current)
            current = []

        # process single line
        raw_data = line.split()
        for item in raw_data:
            k, _ = item.split(':')
            current.append(k)

# don't forget the last one
passports.append(current)

# check validity
count = 0
for passport in passports:
    validity_score = sum([field in passport for field in REQUIRED_FIELDS])
    if validity_score == len(REQUIRED_FIELDS):
        count += 1

print(count)
