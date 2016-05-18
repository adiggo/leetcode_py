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



# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# second round: use a var rather than a list
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.n = None
        self.peekFlag = False
    
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:
            self.n = self.iterator.next()
            self.peekFlag = True
        return self.n

    def next(self):
        """
        :rtype: int
        """
        if not self.peekFlag:
            return self.iterator.next()
        self.peekFlag = False
        nextElement = self.n
        self.n = None
        return nextElement

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekFlag or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
