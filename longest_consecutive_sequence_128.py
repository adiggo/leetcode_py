class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if not nums:
            return 0
        prev = nums[0]
        res = 1
        local_r = 1
        for i in range(1, len(nums)):
            if nums[i] == prev+1:
                local_r += 1
            elif nums[i] == prev:
                continue
            else:
                res = max(res, local_r)
                local_r = 1
            prev = nums[i]
        return max(res, local_r)

class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = sets.Set(nums)
        res, local = 1, 1
        for n in nums:
            r, l = n, n
            local = 1
            while r + 1 in helper:
                local += 1
                helper.remove(r+1)
                r += 1
            while l - 1 in helper:
                local += 1
                helper.remove(l-1)
                l -= 1
            res = max(res, local)
        return res
