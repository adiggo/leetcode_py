class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or s == "":
            return False
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if c == ')':
                    if left != '(':
                        return False
                elif c == '}':
                    if left != '{':
                        return False
                elif c == ']':
                    if left != '[':
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False
