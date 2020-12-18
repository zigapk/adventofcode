def is_wrapped(s):
    depth = 0
    for i in range(len(s)):
        c = s[i]

        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1

        if depth == 0 and i != 0 and i != len(s) - 1:
            return False

    return True


def find_sign_not_nested(s, sign):
    depth = 0
    for i in range(len(s)):
        c = s[i]

        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1

        if c == sign and depth == 0:
            return i

    return None


def calculate(s):
    try:
        return int(s)
    except Exception:
        pass

    if is_wrapped(s):
        return calculate(s[1:-1])

    times_index = find_sign_not_nested(s, '*')

    if times_index is not None:
        return calculate(s[:times_index]) * calculate(s[times_index + 1:])

    plus_index = find_sign_not_nested(s, '+')
    return calculate(s[:plus_index]) + calculate(s[plus_index + 1:])


result = 0
with open('in', 'r') as f:
    for line in f.readlines():
        a = line.strip().replace(' ', '')

        current = calculate(a)

        result += current

print(result)
