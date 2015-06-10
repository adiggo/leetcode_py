# use a and b keep record of the max in i-2, and i-1.
# the dp function should be dp(i) = max(dp(i-2)+ num[i], dp(i-1))
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b= max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if a + nums[i] > b:
                b, a = a+nums[i], b
            else:
                a = b
        return max(a, b)
