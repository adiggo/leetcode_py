class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # same problem as pascal triangle one
        if rowIndex < 0:
            return []
        res = [1]
        if rowIndex < 2:
            return [1,1] if rowIndex == 1 else res
        for i in xrange(rowIndex):
            l = [1]
            for j in xrange(len(res)-1):
                l.append(res[j] + res[j+1])
            l.append(1)
            res = l
        return res


class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # same problem as pascal triangle one
        if rowIndex < 0:
            return []
        res = [1]
        for i in xrange(rowIndex+1):
            if i < 1:
                continue
            res.append(1)
            for j in xrange(len(res)-2 , 0, -1):
                res[j] = res[j] + res[j-1]
        return res
