class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0,0]
        left, right = 0, len(nums)-1
        left_edge, right_edge = -1, -1
        has_edge = False
        while left < right:
            mid = left + (right - left)/2
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        left_edge = left
        if nums[left_edge] == target:
            has_edge = True
        # get right edge
        left, right = 0, len(nums)-1
        while left < right:
            mid = left +(right - left)/2
            if target < nums[mid]:
                right = mid -1
            elif target >= nums[mid]:
                left = mid+1
        right_edge = left
        if not has_edge:
            return [-1, -1]
        else:
            if nums[right_edge] != target:
                right_edge -= 1
            return [left_edge, right_edge]
