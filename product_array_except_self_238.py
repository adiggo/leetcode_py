class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        helper1 = [1] * len(nums)
        helper2 = [1] * len(nums)
        for i in xrange(1, len(nums)):
            helper1[i] = nums[i - 1] * helper1[i - 1]

        for j in xrange(len(nums) - 2, -1, -1):
            helper2[j] = nums[j + 1] * helper2[j + 1]
        for i in xrange(len(nums)):
            nums[i] = helper1[i] * helper2[i]
        return nums

# better approach with O(n) space
class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        helper = [1] * len(nums)
        for i in xrange(1, len(nums)):
            helper[i] = nums[i - 1] * helper[i - 1]
        tmp = 1
        for j in xrange(len(nums) - 2, -1, -1):
            helper[j] = nums[j + 1] * tmp * helper[j]
            tmp = nums[j + 1] * tmp
        return helper
