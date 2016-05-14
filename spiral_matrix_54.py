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




# second round. Use a while loop is much cleaner than the for loop.
# The whole idea is to narrow down from outside to inside.
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
        s_r, e_r, s_c, e_c = 0, row, 0, column
        # iterator
        while s_r < e_r and s_c < e_c:
            # 1, 2, 3
            for i in xrange(s_c, e_c):
                res.append(matrix[s_r][i])
            s_r += 1
            
            # 6 9
            for i in xrange(s_r, e_r):
                res.append(matrix[i][e_c-1])
            e_c -= 1
            
            # 8 7
            if s_r < e_r:
                for i in xrange(e_c-1, s_c-1, -1):
                    res.append(matrix[e_r-1][i])
                e_r -= 1
            # 4
            if s_c < e_c:
                for i in xrange(e_r-1, s_r-1, -1):
                    res.append(matrix[i][s_c])
                s_c += 1
        return res
