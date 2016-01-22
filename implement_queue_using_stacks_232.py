class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # stack push
        self.stack1.append(x)    
        self.size += 1
    

    def pop(self):
        """
        :rtype: nothing
        """
        if self.size == 0:
            return 
        self.size -= 1
        # stack 2 store all the element in the reverse order
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.size > 0:
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2[-1]
            else:
                return self.stack2[-1]
        else:
            return 0

    def empty(self):
        """
        :rtype: bool
        """
        if self.size <= 0:
            return True
        else:
            return False
