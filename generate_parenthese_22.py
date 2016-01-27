class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, '' , res, 0, 0)
        return res
        
        
    def dfs(self, n, p, res, left, right):
        if right > left:
            return
        if left == right and left == n:
            res.append(p)
            return
        if left > n or right > n:
            return
        self.dfs(n, p+'(', res, left + 1, right)
        self.dfs(n, p+')', res, left, right + 1)
