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
