class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) != 9 or len(board[0]) < 9:
            return
        self.dfs(board, 0, 0)
    
    # return boolean    
    def dfs(self, board, r, c):
        if c >= 9:
            return self.dfs(board, r+1, 0)
        if r == 9:
            return True
        if board[r][c] == '.':
            for i in range(9):
                board[r][c] = str(i+1)
                if self.get_valid_nums(board, r, c, board[r][c]):
                    if self.dfs(board, r, c+1):
                        return True
                board[r][c] = '.'
        else:
            return self.dfs(board, r, c+1)
        return False
        
    def get_valid_nums(self, board, r, c, t):
        for i in range(9):
            if i != r and board[i][c] == t:
                return False
        for i in range(9):
            if i != c and board[r][i] == t:
                return False
        for i in range(3*(r/3), 3* (r/3+1)):
            for j in range(3*(c/3), 3*(c/3+1)):
                if (i != r or j != c) and board[i][j] == t:
                    return False
        return True
