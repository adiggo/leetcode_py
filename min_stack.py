class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.helper = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        min_ele = self.getMin()
        if min_ele is None or x < min_ele:
            min_ele = x
        self.stack.append(x)
        self.helper.append(min_ele)

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.helper.pop()
    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return None if not self.helper else self.helper[-1]
