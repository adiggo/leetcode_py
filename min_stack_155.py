class MinStack:

    # initialize your data structure here.
    def __init__(self):
        self.stack = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        min_ele = self.getMin()
        if min_ele is None or x < min_ele:
            min_ele = x
        self.stack.append(Node(x, min_ele))
    # @return nothing
    def pop(self):
        self.stack.pop()
    # @return an integer
    def top(self):
        return self.stack[-1].v

    # @return an integer
    def getMin(self):
        return None if not self.stack else self.stack[-1].min_v

class Node:
    def __init__(self, v, min_v):
        self.v = v
        self.min_v = min_v





# no need to create new class. use a list: first index store the value, second index stores the min element
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            if self.stack[-1][1] < x:
                self.stack.append([x, self.stack[-1][1]])
            else:
                self.stack.append([x, x])
        else:
            self.stack.append([x, x])
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        else:
            return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
