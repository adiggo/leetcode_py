class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        self.dfs(res, [], k, n, 0, 1)
        return res
        
    def dfs(self, res, combination, k, n, sum, index):
        if len(combination) > k or sum > n:
            return
        if len(combination) == k and sum == n:
            res.append(list(combination))
            return
        for i in range(index, 10):
            combination.append(i)
            self.dfs(res, combination, k, n, sum+ i,i+1)
            combination.pop()
