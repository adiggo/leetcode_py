class Solution(object):
    def missingNumber(self, nums):
        if not nums:
            return None
        sum = 0
        for num in nums:
            sum += num
        helper = 0
        for i in range(len(nums)+1):
            helper += i
        return helper - sum
        
