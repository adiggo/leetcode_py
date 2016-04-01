class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left = 0
        i = 0
        while i < len(nums) and left <= i:
            if nums[i] != 0:
                if left != i:
                    nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1

