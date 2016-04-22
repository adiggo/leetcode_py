class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        res = None
        for i in xrange(len(nums)):
            cur = nums[i]
            if cur >= s:
                res = 1
            for j in xrange(i+1, len(nums)):
                cur += nums[j]
                if cur >= s:
                    if res is None or res > j-i+1:
                        res = j - i + 1
                        break
        return res if res is not None else 0



class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        l = self.twoPointer(s, nums) 
        return l
        
    def twoPointer(self, s, nums):
        cur = 0
        start, end = 0, 0
        res = None

        while end < len(nums):
            if cur >= s:
                while cur >= s and start < end:
                    cur -= nums[start]
                    start += 1
                if res is None or end - start + 1 < res:
                    res = end - start + 1
            else:
                cur += nums[end]
                end += 1
        
        if cur >= s:
            while cur >= s and start < end:
                cur -= nums[start]
                start += 1
            if res is None or res > end - start + 1:
                res = end - start + 1
        return res if res is not None else 0
        
        
                
