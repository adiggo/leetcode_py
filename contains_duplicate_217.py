class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None or len(nums) == 0:
            return False
        helper = set()
        for i in xrange(len(nums)):
            if nums[i] in helper:
                return True
            else:
                helper.add(nums[i])
        return False
        
