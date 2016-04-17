class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # one node has two child, one child or none
        # make sure preorder can construct a valid tree
        # left/right
        # This question can be tranformed as whether this node has a valid parent, '#' is not a valid parent
        if not preorder or preorder == '#':
            return True
        stack = []
        i = 0
        # use 1,2, # denote 2
        for c in preorder.split(','):
            if c == '#':
                stack.append(2)
                while self.__checkStack(stack):
                    continue
            else:
                stack.append(1)
        if stack and len(stack) == 1 and stack[0] == 2:
            return True
        else:
            return False
            
    def __checkStack(self, stack):
        if len(stack) >= 3:
            if stack[-1] == 2 and stack[-2] == 2 and stack[-3] == 1:
                stack.pop()
                stack.pop()
                stack[-1] = 2
                return True
        return False
