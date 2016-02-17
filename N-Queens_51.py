class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # need a check valid method
        res = []
        combination = [['.' for i in range(n)] for j in range(n)]
        self.dfs(res, combination, 0, 0, n, 0)
        return res
    
    def dfs(self, res, combination, i, j, n, number):
        if i > n-1 or j > n-1:
            if number == n:
                res.append([''.join(e for e in combination[i]) for i in range(n)])
            return
        if i > number:
            return
        for k in range(n):
            valid = self.isValid(combination, i, k, n)
            if valid:
                combination[i][k] = 'Q'
            else:
                continue
            self.dfs(res, combination, i+1, k, n, number+1 if valid else number)
            combination[i][k] = '.'
        return
    
    def isValid(self, combination, i, j, n):
        # vertical
        for k in range(n):
            if k >= i:
                break
            if combination[k][j] == 'Q':
                return False
        #row
        for k in range(n):
            if k >= j:
                break
            if combination[i][k] == 'Q':
                return False
        # left diagonal check
        for k in range(n):
            if i-k < 0 or j-k < 0:
                break
            if combination[i-k][j-k] == 'Q':
                return False
        for k in range(n):
            if i-k < 0 or j+k >= n:
                break
            if combination[i-k][j+k] == 'Q':
                return False
        return True
