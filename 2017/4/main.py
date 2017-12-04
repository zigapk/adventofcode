import fileinput

s1 = 0
s2 = 0

def has_anagrams(word_list):
    s = set()
    for word in word_list:
        if not str(sorted(word)) in s:
            s.add(str(sorted(word)))
        else:
            return True
    return False

for line in fileinput.input():
    line = line.split()
    if len(line) == len(set(line)): s1 += 1
    if not has_anagrams(line): s2 += 1

print(s1)
print(s2)
