s is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # record current level index
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        # optional
        if self.hasNext():
            curList, index = self.stack[-1]
            cur = curList[index].getInteger()
            self.stack[-1][-1] += 1
            return cur
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            curList, index = self.stack[-1]
            if index >= len(curList):
                self.stack.pop()
            else:
                if not curList[index].isInteger():
                    self.stack[-1][-1] += 1
                    self.stack.append([curList[index].getList(), 0])
                else:
                    return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next()) 
