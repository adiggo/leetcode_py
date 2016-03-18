class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # convert 0 to 2 if dead transform to live cell
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 1:
                    count = self.checkOneNum(board, i, j, m, n)
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 0:
                    count = self.checkOneNum(board, i, j, m, n)
                    if count == 3:
                        board[i][j] = 3
        # 2 denotes dead and 3 denotes live in next generation
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
                    
                    
    def checkOneNum(self, board, i, j, m , n):
        count = 0
        for k in xrange(j-1, j+2):
            if k < n and k >= 0:
                if i - 1 >= 0:
                    if board[i-1][k] == 1 or board[i-1][k] == 2:
                        count += 1
                if i + 1 < m:
                    if board[i+1][k] == 1 or board[i+1][k] == 2:
                        count += 1
                if k != j:
                    if board[i][k] == 1 or board[i][k] == 2:
                        count += 1
        return count
