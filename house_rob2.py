class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        # n^2 time complexity
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        size = len(nums)
        max_value = max(nums[0], nums[1])
        for i in range(0, len(nums)):
            first = nums[i]
            #edge check
            second = max(nums[i], nums[i+1]) if i < len(nums)-1 else max(nums[i], nums[0])
            max_value = max(max_value, second)
            for  j in range(i+2, i+size-1):
                index = j
                if j > size -1:
                    index = j-size
                if nums[index] + first > second:
                    first, second =second, nums[index] + first
                else:
                    first = second
            max_value = max(second, max_value)
        return max_value
