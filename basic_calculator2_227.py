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
                    d = 0
                    while i < len(s) and s[i] <= '9' and s[i] >= '0':
                        d, i = d * 10 + int(s[i]), i+1
                    stack.append(d)
                elif s[i] == '*' or s[i] == '/':
                    ops, first, second, i  =s[i], stack.pop(), 0, i+1
                    while s[i] == ' ':
                        i += 1
                    while i < len(s) and s[i] <= '9' and s[i] >= '0':
                        second, i = second * 10 + int(s[i]), i+1
                    tmp = first / second if ops == '/' else first*second
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



# second round
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stack, i = [], 0
        while i < len(s):
            if s[i] != ' ':
                if s[i] == '+':
                    i += 1
                    d, i = self.get_digit(s, i)
                    stack.append(d)
                elif s[i] == '-':
                    i += 1
                    d, i = self.get_digit(s, i)
                    stack.append(-d)
                elif s[i] == '*' or s[i] == '/':
                    op = s[i]
                    i += 1
                    d, i = self.get_digit(s, i)
                    d = self.arithmetic(stack.pop(), d, op)
                    stack.append(d)
                else:
                    # the first number
                    d, i = self.get_digit(s, i)
                    stack.append(d)
            else:
                i += 1
        res = 0
        while stack:
            res += stack.pop()
        return res
        
    def arithmetic(self, n1, n2, op):
        if op == '*':
            return n1 * n2
        elif op == '/':
            res = n1 / n2
            # python division always floor.
            return res if res >= 0 else int(math.ceil(float(n1)/n2))
        else:
            raise Exception('operator other than * and / is not allowed')
    
    def get_digit(self, s, s_i):
        while s[s_i] == ' ':
            s_i += 1
        d = 0
        while s_i < len(s) and s[s_i].isdigit():
            d = 10 * d + int(s[s_i])
            s_i += 1
        return d, s_i
        
