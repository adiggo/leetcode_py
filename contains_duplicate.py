class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None or len(nums) == 0:
            return False
        helper = {}
        for i in range(len(nums)):
            helper[nums[i]] = 0

        if len(helper) < len(nums):
            return True
        else:
            return False
