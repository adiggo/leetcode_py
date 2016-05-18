class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right] and nums[left] == nums[right]:
                left = left + 1
                right = right - 1
            else:
                right = mid
        return nums[right]
# second round
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right = right - 1
            else:
                right = mid
        return nums[right]
