class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for x in range(n)] for x in range(n)]
        v = 1
        for i in range(n/2):
            for j in range(i, n-i-1):
                res[i][j] = v
                res[j][n-i-1] = v + (n-2*i-1)
                res[n-i-1][n-1-j] = v+2*(n-2*i-1)
                res[n-j-1][i] = v+3*(n-2*i-1)
                v += 1
            v += 3 * (n-2*i-1) 
        if n % 2 == 1:
            res[n/2][n/2] = n**2 
        return res
