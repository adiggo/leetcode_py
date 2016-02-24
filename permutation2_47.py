class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(res, [], nums, [False] * len(nums))
        return res

    def dfs(self, res, cur, nums, used):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        if len(cur)  > len(nums):
            return
        for j in range(len(nums)):
            if used[j] or (j>0  and nums[j] == nums[j-1] and not used[j-1]):
                continue
            else:
                used[j] = True
            cur.append(nums[j])
            self.dfs(res, cur, nums, used)
            cur.pop()
            used[j] = False
