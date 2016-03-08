class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix[0])==0:
            return []
        row = len(matrix)
        column = len(matrix[0])
        res = []
        for i in range(min(row-1, column-1)/2 + 1):
            # 1,2,3
            if column - i -1 == i:
                for j in range(i,row-i):
                    res.append(matrix[j][i])
                break
            for j in range(i, column-i):
                res.append(matrix[i][j])
            
            # 6
            for j in range(i+1, row-i-1):
                res.append(matrix[j][column-i-1])
            # 9, 8
            
            for j in range(column-i-1, i, -1):
                if row-i-1 == i:
                    continue
                res.append(matrix[row-i-1][j])
            # 7, 4
            for j in range(row-1-i, i, -1):
                if i == column-i-1:
                    continue
                res.append(matrix[j][i])
        return res
