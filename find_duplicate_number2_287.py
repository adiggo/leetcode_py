#O(n * logn)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums)-1
        while start <= end:
            mid = start + (end - start)/2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start

#reference: https://leetcode.com/discuss/89038/o-32-n-solution-using-bit-manipulation-in-10-lines
# O(32*n)
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        start, end = 1, len(nums)-1
        for i in xrange(32):
            a, b = 0, 0
            bit = 1 << i
            for j in xrange(len(nums)):
                if j & bit:
                    a += 1
                if nums[j] & bit:
                    b += 1
            if b > a:
                res += bit
        return res
