class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # record block by block(between negative), special case 0
        if not nums:
            return 0
        curMin, curMax = nums[0], nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):
            tmp = curMax
            curMax = max(nums[i], nums[i] * curMin, nums[i] * curMax)
            curMin = min(nums[i], nums[i] * curMin, nums[i] * tmp)
            res = max(curMax, curMin, res)
        return res
