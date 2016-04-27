class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap should resolve this question
        # k size heap
        if not nums:
            return []
        queue =collections.deque()
        res = []
        for i in xrange(len(nums)):
            queue.append(nums[i])
            if len(queue) == k:
                res.append(max(queue))
                queue.popleft()
        return res



    def maxSlidingWindow2(self, nums, k):
        dp = collections.deque()
        res = []
        # keep the first index in the dp as the max value of the sliding window
        for i in range(len(nums)):
            while dp and nums[dp[-1]] < nums[i]:
                dp.pop()
            dp.append(i)
            # the first element is not used any more
            if dp[0] == i-k:
                dp.popleft()
            # append the sub-max-value into result
            if i >= k-1:
                res.append(nums[dp[0]])
        return res
        
