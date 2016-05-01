class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # handle special case
        nums = [1] + nums + [1]
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
        # from 1 to n inclusive, since the first one is the left boundary
        return self.memorization(1, n, dp, nums)
    
    def memorization(self, i, j, dp, nums):
        if dp[i][j] > 0:
            return dp[i][j]
        for x in xrange(i, j+1):
            dp[i][j] = max(dp[i][j], self.memorization(i, x-1, dp, nums) + nums[i-1] * nums[x]*nums[j+1] + self.memorization(x+1, j, dp, nums))
        return dp[i][j]
        
        
        
