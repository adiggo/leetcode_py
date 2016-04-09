class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        y = len(matrix[0]) - 1
        # O(m+n)
        for x in xrange(len(matrix)):
            while matrix[x][y] > target and y:
                y -= 1
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                return False
        return False
               

#reference: https://leetcode.com/discuss/47528/c-with-o-m-n-complexity
# running time:T(n) = 3*T(n/2) +c
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        return self.helper(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, target)
        
    def helper(self, matrix, rowStart, rowEnd, colStart, colEnd, target):
        if rowStart > rowEnd or colStart > colEnd:
            return False
        rowM, colM = rowStart + (rowEnd-rowStart)/2, colStart + (colEnd-colStart)/2
        if matrix[rowM][colM] == target:
            return True
        elif matrix[rowM][colM] > target:
            return self.helper(matrix, rowStart, rowM-1, colStart, colM-1, target) or self.helper(matrix, rowStart, rowM-1, colM, colEnd, target) or self.helper(matrix, rowM, rowEnd, colStart, colM -1 , target)
        else:
            return self.helper(matrix, rowStart, rowM-1, colM+1, colEnd, target) or self.helper(matrix, rowM+1, rowEnd, colStart, colM, target) or self.helper(matrix, rowM, rowEnd, colM+1, colEnd, target)
