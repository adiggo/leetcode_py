class Solution(object):
    def __init__(self):
        self.num = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        combination = [['.' for i in range(n)] for j in range(n)]
        self.dfs(combination, 0, 0, n, 0)
        return self.num
    
    def dfs(self, combination, i, j, n, number):
        if i > n-1 or j > n-1:
            if number == n:
                self.num += 1
            return
        if i > number:
            return
        for k in range(n):
            valid = self.isValid(combination, i, k, n)
            if valid:
                combination[i][k] = 'Q'
            else:
                continue
            self.dfs(combination, i+1, k, n, number+1 if valid else number)
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
