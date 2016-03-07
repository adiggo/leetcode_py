class Solution(object):
    def wiggle_sort(self, nums):
        if not nums:
            return
        nums.sort()
        # wiggle sort need consider 3 number as a whole
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
