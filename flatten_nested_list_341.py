# reference:https://leetcode.com/discuss/95934/real-iterator-in-python-java-c
# stack record the cur level list and index, index is the index in cur level.
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        # cur level index + 1
        self.stack[-1][1] += 1

        return nestedList[i].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            # get cur level list and its index
            nestedList, i = s[-1]
            # cur level index equal to length, then just pop out cur level list
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                # return true since cur element is integer
                if x.isInteger():
                    return True
                # if cur element is not integer, then let curlevel index + 1
                s[-1][1] += 1
                # append the list, update cur level
                s.append([x.getList(), 0])
        return False
