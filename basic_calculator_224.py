class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        stack = []
        stack.append(0)
        stack.append('+')
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                stack.append(s[i])
                i += 1
            elif s[i] == '(':
                stack.append(0)
                stack.append('+')
                i += 1
            elif s[i] == ')':
                cur = stack.pop()
                ops = stack.pop()
                prev = stack.pop()
                if ops == '+':
                    stack.append(prev + cur)
                elif ops == '-':
                    stack.append(prev - cur)
                i += 1
            elif s[i] <= '9' and s[i] >= '0':
                num = 0
                while i < len(s) and s[i] <= '9' and s[i] >= '0':
                    num = 10 * num + int(s[i])
                    i += 1
                ops = stack.pop()
                prev = stack.pop()
                if ops == '+':
                    stack.append(prev + num)
                elif ops == '-':
                    stack.append(prev - num)
            else:
                i += 1
        return stack.pop()
