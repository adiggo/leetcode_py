class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = [0 for x in xrange(len(nums))]
        if nums:
            self.dp[0] = nums[0]
            for i in xrange(1, len(nums)):
                self.dp[i] = (self.dp[i-1] + nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.dp[j] - self.dp[i-1] 
        else:
            return self.dp[j]
