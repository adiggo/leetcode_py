'''
special case: in python, it is flooring for int. but in c it is flooring to 0. 
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                d1 = stack.pop()
                d2 = stack.pop()
                if t == '+':
                    summation = d1 + d2
                    stack.append(summation)
                elif t == '-':
                    minus = d2 - d1
                    stack.append(minus)
                elif t == '*':
                    multiplication = d1 * d2
                    stack.append(multiplication)
                elif t == '/':
                    if d2 * d1 < 0:
                        stack.append(-(-d2/d1))
                    else:
                        stack.append(d2/d1)
            else:
                stack.append(int(t))
        return stack.pop()
