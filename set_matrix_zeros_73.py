class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        f1, f2 = False, False
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            if matrix[i][0] == 0:
                f1 = True
                break
        
        for j in xrange(n):
            if matrix[0][j] ==0:
                f2 = True
                break
        
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                matrix[i][j] = 0 if matrix[0][j] == 0 or matrix[i][0] == 0 else matrix[i][j]
        
        for i in xrange(m):
            if f1:
                matrix[i][0] = 0
        
        for j in xrange(n):
            if f2:
                matrix[0][j] = 0
