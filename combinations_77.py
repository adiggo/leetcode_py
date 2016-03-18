class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # the requirement is k numbers
        res = []
        self.dfs(n, k , 0, res, [])
        return res
        
    def dfs(self, n, k, index, res, cur):
        if len(cur) == k:
            res.append(list(cur))
        for i in range(index, n):
            cur.append(i+1)
            self.dfs(n, k , i+1, res, cur)
            cur.pop()
