class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = 0
        prev = 0
        for i in xrange(0, len(nums)):
            # prev --> max money by nums[i-2]
            # cur ---> max money by nums[i-1]
            tmp = prev + nums[i]
            prev = max(prev, cur)
            cur = tmp
        return max(cur, prev)


#second round
class Solution2(object):
        def rob(self, nums):
                    """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
                        return 0
        pprev, prev = 0, 0
        for num in nums:
                        tmp = prev
            prev = num + pprev
            pprev = max(pprev, tmp)
        
        return max(prev, pprev)
