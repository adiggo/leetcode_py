class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w, l = len(grid), len(grid[0])
        dp = [[0 for x in range(l)] for x in range(w)]
        dp[0][0] = grid[0][0]
        for i in range(1, w):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, l):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, w):
            for j in range(1, l):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[w-1][l-1]
