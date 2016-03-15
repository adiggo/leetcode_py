class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for x in range(c)] for x in range(r)]
        flag = False        
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                flag = True
            else:
                dp[0][i] = 0 if flag else 1
        flag = False 
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                flag = True
            else:
                dp[i][0] = 0 if flag else 1
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[r-1][c-1]
        
