class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, size = self.dfs(nums, 0)
        return res

    def dfs(self, nums, index):
        if index >= len(nums):
            return [[]], 0
        res, size = self.dfs(nums, index + 1)
        r = list(res)
        for i in range(len(res)):
            cur = res[i]
            if index < len(nums) - 1 and nums[index] == nums[index + 1]:
                if i >= size:
                    r.append([nums[index]] + cur)
            else:
                r.append([nums[index]] + cur)
        return r, len(res)
