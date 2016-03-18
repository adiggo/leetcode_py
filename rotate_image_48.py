class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m / 2):
            # start from top to right, record right
            tmp1 = [e[n - 1 - i] for e in matrix[i: n - i]]
            tmp2 = matrix[n - 1 - i][i: n - i]
            tmp2.reverse()
            tmp3 = [e[i] for e in matrix[i:n - i]]
            tmp3.reverse()
            tmp4 = matrix[i][i: n - i]
            for j in xrange(i, n - i):
                matrix[j][n - 1 - i] = tmp4[j - i]
            # start from right to bottom, record bottom
            for j in xrange(i, n - i):
                matrix[n - 1 - i][n - 1 - j] = tmp1[j - i]
            # start from bottom to left, record left
            for j in xrange(i, n - i):
                matrix[n - 1 - j][i] = tmp2[j - i]
            # start from left to top
            for j in xrange(i, n - i):
                matrix[i][j] = tmp3[j - i]


# transpose and reverse
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # transpose
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse
        for i in range(m):
            for j in range(n/2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j] 

# simplified api, rotate point to point
    def rotatei3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m / 2):
            # start from top to right, record right
            l = m - 2*i - 1
            for j in xrange(l):
                tmp = matrix[i][i+j]
                matrix[i][i+j] = matrix[i+l-j][i]
                matrix[i+l-j][i] = matrix[i+l][i+l-j]
                matrix[i+l][i+l-j] =  matrix[i+j][i+l]
                matrix[i+j][i+l] = tmp

