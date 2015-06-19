class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        # set priority
        # use a stack
        helper = []
        num = 0
        sum = 0
        for i in range(len(s)):
            if s[i] != ')':
                # if c is a digit
                if '9' >= s[i] >= '0':
                    num = 10 * num + int(s[i])
                    if i + 1 < len(s):
                        if s[i+1] > '9' or s[i+1] < '0':
                            helper.append(num)
                            num = 0
                        else:
                            continue
                    else:
                        helper.append(num)

                if s[i] == ' ':
                    num = 0
                    continue
                if s[i] == '+' or s[i] == '-' or s[i] == '(':
                    helper.append(s[i])
            else:
                subsum = 0
                cur_stack = []
                a = helper.pop()
                while a != '(':
                    cur_stack.append(a)
                    a = helper.pop()
                j = len(cur_stack) -1
                while j >= 0:
                    if cur_stack[j] != "+" and cur_stack[j] != "-":
                        subsum += cur_stack[j]
                        j -= 1
                    elif cur_stack[j] == "+":
                        subsum += cur_stack[j-1]
                        j -= 2
                    elif cur_stack[j] == "-":
                        subsum -= cur_stack[j-1]
                        j -= 2
                helper.append(subsum)

        j = 0
        while j < len(helper):
            if helper[j] != '+' and helper[j] != '-':
                sum += int(helper[j])
                j += 1
            elif helper[j] == '+':
                sum += int(helper[j+1])
                j += 2
            elif helper[j] == '-':
                sum -= int(helper[j+1])
                j += 2
        return sum
