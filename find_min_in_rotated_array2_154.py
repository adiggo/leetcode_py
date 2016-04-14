class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # worse running time might be O(n)
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left)/2
            # the reason here why we compare with nums[right] is because mid is left if left + 1== right
            if nums[mid] < nums[right]:
                right = mid
            # add this condition for equal case
            elif nums[mid] > nums[right]:
                left = left + 1
            else:
                right -= 1
        return nums[left]




