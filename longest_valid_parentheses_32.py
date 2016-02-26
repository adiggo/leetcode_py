class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # local left and local right
        left, right= 0, 0
        # stack to record local's longest valid length
        stack = []
        # 0 is used for special case, insert when left > right
        for p in s:
            if p == '(':
                left += 1
            if p == ')':
                right += 1
            if left == right:
                stack.append(2 * min(left, right))
            if left > right:
                if p == '(':
                    stack.append(0)
                if p == ')':
                    local = 2
                    while stack[-1] != 0:
                        local += stack.pop()
                    stack.pop()
                    if not stack:
                        stack.append(local)
                    else:
                        while stack[-1] != 0:
                            local += stack.pop()
                        stack.append(local)
            if right > left:
                left, right = 0, 0
        # in the end part of input, it might have more left parenthese than right.
        return max(stack) if stack else 0
