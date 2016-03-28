class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows <= 0:
            return res
        res.append([1])
        for i in xrange(1, numRows):
            if i == 1:
                res.append([1,1])
            else:
                l = []
                l.append(1)
                for j in xrange(len(res[-1]) - 1):
                    l.append(res[-1][j] + res[-1][j+1])
                l.append(1)
                res.append(l)
        return res
