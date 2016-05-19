# https://leetcode.com/discuss/81877/java-14ms-relative-short-solution-with-explanation-time-space
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        # use an additional array to mark the position we have already visited
        # pass the target value to current position
        m, n = len(matrix), len(matrix[0])
        visited = [[0 for x in xrange(n)] for x in xrange(m)]
        res = 1
        for i in xrange(m):
            for j in xrange(n):
                res = max(res, self.findConsecutivePath(matrix, visited, matrix[i][j], i, j))
        return res

    def findConsecutivePath(self, matrix, visited, target, i, j):
        if visited[i][j] > 0:
            return visited[i][j]
        l1, l2, l3, l4 = 1, 1, 1, 1
        if i - 1 >= 0 and matrix[i-1][j] < target:
            l1 = 1 + self.findConsecutivePath(matrix, visited, matrix[i-1][j], i-1, j)
        if i+1 < len(matrix) and matrix[i+1][j] < target:
            l2 = 1 + self.findConsecutivePath(matrix, visited, matrix[i+1][j], i+1, j)
        if j -1 >= 0 and matrix[i][j-1] < target:
            l3 = 1 + self.findConsecutivePath(matrix, visited, matrix[i][j-1], i, j-1)
        if j + 1 < len(matrix[0]) and matrix[i][j+1] < target:
            l4 = 1 + self.findConsecutivePath(matrix, visited, matrix[i][j+1], i, j+1)
        res = max(l1, l2, l3, l4)
        visited[i][j] = res
        return res
