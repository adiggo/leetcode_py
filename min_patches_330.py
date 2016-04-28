#reference: https://leetcode.com/discuss/82822/solution-explanation
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # curSum should cover 1 to n
        index, curSum, ans = 0, 1, 0
        size = len(nums)
        while curSum <= n:
            if index < size and nums[index] <= curSum:
                curSum += nums[index]
                index += 1
            else:
                curSum <<= 1
                ans += 1
        return ans
