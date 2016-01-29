class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = nums[0]
        length = 1
        for i, num in enumerate(nums[1:]):
            if num != prev:
                nums[length] = num
                length += 1
                prev = num
        return length
