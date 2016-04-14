class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.dp = []
        else:
            m, n = len(matrix), len(matrix[0])
            self.dp = [ [0 for x in xrange(n+1)] for x in xrange(m+1) ]
            for i in xrange(1, m+1):
                for j in xrange(1, n+1):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[max(row1+1, row2+1)][max(col1+1, col2+1)] - self.dp[min(row1+1, row2+1)-1][max(col1+1, col2+1)] - self.dp[max(row1+1, row2+1)][min(col1+1, col2+1)-1] + self.dp[min(row1+1, row2+1)-1][min(col1+1, col2+1)-1]


