class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # find left and right bound
        i = 0
        res = []
        l = len(nums)
        while i < l:
            if i == l-1:
                res.append(str(nums[-1]))
                return res
            first = i
            while i < l - 1 and nums[i]+1 == nums[i+1]:
                i += 1
            left = nums[first]
            right = nums[i]
            if first == i:
                res.append(str(left))
            else:
                res.append(str(left) + '->' + str(right))
            i += 1
        return res
