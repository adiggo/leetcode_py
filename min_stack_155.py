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
