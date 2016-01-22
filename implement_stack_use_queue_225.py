class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = []
        self.size = 0
    # @param x, an integer
    # @return nothing
    def push(self, x):
        helper = []
        helper.append(x)
        while self.q:
            helper.append(self.q.pop(0))
        self.size += 1
        # reset q
        self.q = helper

    # @return nothing
    def pop(self):
        if self.size <= 0:
            return
        else:
            self.q.pop(0)
            self.size -= 1

    # @return an integer
    def top(self):
        if self.size > 0:
            return self.q[0]
        else:
            return 0
    # @return an boolean
    def empty(self):
        return self.size <= 0
