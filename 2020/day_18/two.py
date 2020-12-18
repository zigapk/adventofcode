class Plus:
    def __init__(self, s):
        self.s = s
        self.nested = False
        try:
            self.val = int(s)
            self.operator = None
            self.left = None
            self.right = None
        except Exception:
            self.val = None

            operator_index = None
            while operator_index is None:
                operator_index = self.find_last_not_nested_operator_index()
                if operator_index is None:
                    self.s = self.s[1:-1]
                    self.nested = True

            self.operator = self.s[operator_index]
            self.left = Plus(self.s[:operator_index])
            self.right = Plus(self.s[operator_index + 1:])

    def find_last_not_nested_operator_index(self):
        depth = 0
        for i in range(len(self.s) - 1, -1, -1):
            c = self.s[i]

            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif (c == '+') and depth == 0:
                return i

        return None

    def to_string(self):
        if self.val is not None:
            return str(self.val)
        else:
            res = '(' + self.left.to_string() + '+' + self.right.to_string() + ')'
            
            return res
            
            # def value(self):
    #     if self.val is not None:
    #         # print(self.s, '=', self.val)
    #         return self.val
    #     if self.operator == '+':
    #         self.val = self.left.value() + self.right.value()
    #         # print(self.s, '=', self.val)
    #         return self.val
    #     elif self.operator == '*':
    #         self.val = self.left.value() * self.right.value()
    #         # print(self.s, '=', self.val)
    #         return self.val
    #     raise


result = 0
with open('sample', 'r') as f:
    for line in f.readlines():
        a = line.strip().replace(' ', '')
        current = eval(Plus(a).to_string())

        print(current)
        result += current

print(result)
