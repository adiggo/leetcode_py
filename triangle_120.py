class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # top to bottom or bottom to top --> same
        # i-1, i
        res = 0
        if not triangle:
            return 0
        prev = []
        for i in xrange(len(triangle)-1, -1, -1):
            if i == len(triangle)-1:
                prev.extend(triangle[i])
            else:
                l = len(triangle[i])
                cur = []
                for j in xrange(l):
                    prev[j] = triangle[i][j] + min(prev[j], prev[j+1])
                prev.pop()
        return min(prev)
