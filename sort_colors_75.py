class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left, right = 0, len(nums) - 1
        # iterator
        index = 0
        while index <= right:
            if nums[index] == 1:
                index += 1
                continue
            elif nums[index] == 0:
                if left != index:
                    nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
        return
