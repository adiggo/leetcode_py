
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None or len(nums) == 0:
            return False
        nums = sorted(nums)
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            else:
                prev = nums[i]
                continue
        return False
