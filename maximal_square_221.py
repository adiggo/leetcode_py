class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        # resuse the largest historgram code
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
                    min_l = min(width, heights[k])
                    res = max(res, min_l * min_l)
                    i -= 1
            i += 1
        while stack:
            k = stack.pop()
            # the first element in the stack should be the smallest element
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            min_l = min(width,  heights[k])
            res = max(res, min_l * min_l)
        return res
                   


    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquareDP(self, matrix):
        if not matrix:
            return 0
        # resuse the largest historgram code
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * n for x in xrange(m)]
        for i in xrange(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = max(res, dp[i][0])
                
        for i in xrange(n):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                res = max(res, dp[0][i])
                
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    res = max(res, dp[i][j] * dp[i][j])
        return res
