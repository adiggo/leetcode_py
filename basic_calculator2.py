class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stack, i = [], 0
        while i < len(s):
            if s[i] != ' ':
                if s[i] == '+' or s[i] == '-':
                    stack.append(s[i])
                    i += 1
                elif s[i] <= '9' and s[i] >= '0':
                    tmp = 0
                    while i < len(s) and s[i] <= '9' and s[i] >= '0':
                        tmp, i = tmp * 10 + int(s[i]), i+1
                    stack.append(tmp)
                elif s[i] == '*' or s[i] == '/':
                    operator, first, second, i  =s[i], stack.pop(), 0, i+1
                    while s[i] == ' ':
                        i += 1
                    while i < len(s) and s[i] <= '9' and s[i] >= '0':
                        second, i = second * 10 + int(s[i]), i+1
                    tmp = first / second if operator == '/' else first*second
                    stack.append(tmp)
            else:
                i += 1
        res, j = 0, 0
        while j < len(stack):
            if stack[j] == '+' or stack[j] == '-':
                res, j = res + stack[j+1] if stack[j] == '+' else res-stack[j+1], j+2
            else:
                res, j = res+stack[j], j+1
        return res
