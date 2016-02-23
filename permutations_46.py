class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], nums)
        return res
    
    def dfs(self, res, cur, nums):
        if len(cur) == len(nums):
            res.append(list(cur))
        for j in range(len(nums)):
            if nums[j] in cur:
                continue
            cur.append(nums[j])
            self.dfs(res, cur, nums)
            cur.pop()



# better approach
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs2(res, [], nums, [False] * len(nums))
        return res
    
    def dfs2(self, res, cur, nums, used):
        if len(cur) == len(nums):
            res.append(list(cur))
        for j in range(len(nums)):
            if used[j]:
                continue
            else:
                used[j] = True
            cur.append(nums[j])
            self.dfs2(res, cur, nums, used)
            used[j] = False
            cur.pop()
