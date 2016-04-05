class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = 0
        summation = 0
        for i in xrange(len(nums)):
            summation += i+1
            helper += nums[i]
        return summation-helper
