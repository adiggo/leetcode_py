class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the break i
        break_p = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] - nums[i-1] > 0:
                break_p = i-1
                break
        min_diff = sys.maxint
        if break_p != -1:
            for i in range(len(nums)-1, break_p, -1):
                if nums[break_p] < nums[i]:
                    tmp = nums[break_p]
                    nums[break_p] = nums[i]
                    nums[i] = tmp
                    break
        left, right = break_p+1, len(nums) -1 
        while left <= right :
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
