class Solution(object):
   # back tracking: not good for running time 
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        res = [0]
        self.back_track(dungeon, 0, 0, res, 0)
        return abs(res[0])
        
    def back_track(self, dungeon, i, j, res, cur_sum):
        cur_sum += dungeon[i][j]
        res[0] = min(res[0], cur_sum)
        if i+1 < len(dungeon):
            self.back_track(dungeon, i+1, j, res, cur_sum)
        if j + 1 < len(dungeon[0]):
            self.back_track(dungeon, i, j+1, res, cur_sum)
           

# dp, build from end
class Solution2:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 0
        m, n = len(dungeon), len(dungeon[0])
        # min-hp needed for each position to get to end
        dp = [[0] * n for x in xrange(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in xrange(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in xrange(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                right = max(dp[i][j + 1] - dungeon[i][j], 1)
                down = max(dp[i + 1][j] - dungeon[i][j], 1)
                dp[i][j] = min(right, down)
        return dp[0][0]
 
