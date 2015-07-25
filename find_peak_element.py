class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        # it is a peak if it larger than left and right
        if not nums or len(nums) == 1:
            return 0
        prev = nums[0]
        index = 1
        while index < len(nums):
            # inital case
            if index == 1:
                if prev > nums[index]:
                    return 0
            # no edge case yet
            if nums[index] > prev and index < len(nums)-1 and nums[index] > nums[index+1]: 
                return index
            # edge case:
            if index == len(nums)-1 and nums[index] > prev:
                return index
            index, prev = index+1, nums[index]
        return nums[-1]
