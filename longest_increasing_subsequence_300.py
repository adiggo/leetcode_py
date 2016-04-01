class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i - 1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)


#nlogn solution for LIS
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sorted_l = []
        for num in nums:
            k = self.findLowerBound(sorted_l, num)
            if k >= len(sorted_l):
                sorted_l.append(num)
            else:
                sorted_l[k] = num
        return len(sorted_l)
        
        
    def findLowerBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)/2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
