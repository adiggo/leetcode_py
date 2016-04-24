class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        # resuse the largest historgram code
        heights = [[0 for x in xrange(len(matrix))] for x in xrange(len(matrix[0]))]
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in xrange(m):
            for j in xrange(n):
                matrix[i][j] = int(matrix[i][j])
                if i == 0:
                    continue
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + matrix[i-1][j]
            res = max(self.largestRectangleArea(matrix[i][:]), res)
        res = max(self.largestRectangleArea(matrix[0][:]), res)
        return res
        
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # when increase put value into stack
        # when decrease pop value larger than cur value
        # the idea is to try each location
        # for the increasing sequence, we can easier get height and width
        # for the decrease part, we need get its neightbor greater part
        stack = []
        res = 0
        i = 0
        while i < len(heights):
            if not stack:
                stack.append(i)
            else:
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    k = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, width * heights[k])
                    i -= 1
            i += 1
        while stack:
            k = stack.pop()
            # the first element in the stack should be the smallest element
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            res = max(res, width * heights[k])
        return res
