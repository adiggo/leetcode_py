class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                m1 = stack.pop()
                m2 = stack.pop()
                stack.append(m2 - m1)
            elif tokens[i] == "/":
                m1 = stack.pop()
                m2 = stack.pop()
                stack.append(int(m2*0.1 / m1))
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(tokens[i]))
        print len(stack)
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
g = Solution()
print g.evalRPN(tokens)

