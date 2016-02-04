class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) -1
        if len(nums) == 1:
            return 1 if nums[0] < target else 0
        while left < right:
            mid = left + (right - left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        return left + 1 if nums[left] < target else left

    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
