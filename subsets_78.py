class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.dfs(nums, 0)
        
        
    def dfs(self, nums, index):
        if index >= len(nums):
            return [[]]
        res = self.dfs(nums, index + 1)
        r = list(res)
        for cur in res:
            r.append([nums[index]] + cur)
        return r
