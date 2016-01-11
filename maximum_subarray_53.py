# use dp to record the sub sum ending in current index
# if current value is positive, also if dp[i-1] is positive too, then just add on. else use the current value as dp[cur]
# if current value is negative, then compare dp[cur-1] with current value, if the sum of these two is larger than 0, then we record dp[cur] = dp[cur] + v. else dp[cur] = v 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        max_sum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            if v >= 0:
                dp[i] = dp[i-1] + v if dp[i-1] > 0 else v
            else:
                dp[i] = dp[i-1] + v if dp[i-1] + v > 0 else v
            max_sum = max(max_sum, dp[i])
        return max_sum
