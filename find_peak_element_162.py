class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            prev = nums[i-1] if i-1 >= 0 else None
            next = nums[i+1] if i+1 < len(nums) else None
            cur = nums[i]
            if cur > prev and cur > next:
                return i
        return -1
