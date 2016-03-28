class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.l = collections.deque()
    
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.l:
            return self.l[0]
        else:
            if self.iterator.hasNext():
                v = self.iterator.next()
                self.l.append(v)
                return v
            else:
                return None

    def next(self):
        """
        :rtype: int
        """
        if self.l:
            return self.l.popleft()
        else:
            if self.iterator.hasNext():
                return self.iterator.next()
            else:
                return None
                
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.l) > 0 or self.iterator.hasNext()
