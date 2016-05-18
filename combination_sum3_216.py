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

# second round
class Solution2(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], 0, res)
        return res
        
        
    def dfs(self, k, n, index, curList, curSum, res):
        if curSum > n:
            return
        if len(curList) == k:
            if curSum == n:
                res.append(list(curList))
            return
        
        for i in xrange(index, 10):
            curList.append(i)
            self.dfs(k, n, i+1, curList, curSum + i, res)
            curList.pop()
        
