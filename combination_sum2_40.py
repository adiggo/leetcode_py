class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combination, res = [], set()
        self.dfs(candidates, target, combination, res, 0, 0)
        return [list(t) for t in res]
        
    def dfs(self, candidates, target, combination, res, sum, index):
        if sum > target:
            return
        if sum == target:
            res.add(tuple(combination))
            return
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target, combination, res, sum+candidates[i], i+1)
            combination.pop()
