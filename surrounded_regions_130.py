class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing
    def solve(self, board):

        def dfs(i, j):
            if i > m - 1 or j > n - 1 or i < 0 or j < 0:
                return
            if i > 1 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'Y'
                dfs(i - 1, j)
            if i < m - 2 and board[i + 1][j] == 'O':
                board[i + 1][j] = 'Y'
                dfs(i + 1, j)
            if j > 1 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'Y'
                dfs(i, j - 1)
            if j < n - 2 and board[i][j + 1] == 'O':
                board[i][j + 1] = 'Y'
                dfs(i, j + 1)

        if not board:
            return
        m, n = len(board), len(board[0])
        # mark the element not surrounded by 'X' as 'N'
        # convert all remaining '0' to 'X'
        # check start from boundary
        for i in xrange(m):
            if board[i][0] == 'O':
                board[i][0] = 'Y'
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                board[i][n - 1] = 'Y'
                dfs(i, n - 1)

        for j in xrange(1, n - 1):
            if board[0][j] == 'O':
                board[0][j] = 'Y'
                dfs(0, j)
            if board[m - 1][j] == 'O':
                board[m - 1][j] = 'Y'
                dfs(m - 1, j)

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
