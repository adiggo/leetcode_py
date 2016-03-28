class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = 0
        prev = 0
        for i in xrange(0, len(nums)):
            tmp = prev + nums[i]
            prev = max(prev, cur)
            cur = tmp
        return max(cur, prev)
