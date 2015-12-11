class Solution:
    def productExceptSelf(self, nums):
        size = len(nums)
        left, right = 1, 1
        helper= [1] * size
        
        for i in range(size -1):
            left *= nums[i]
            helper[i+1] *= left

        for i in range(size-1, 0, -1):
            right *= nums[i]
            helper[i-1] *= right

        return helper




