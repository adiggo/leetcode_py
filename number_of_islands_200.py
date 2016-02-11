class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        visited = [ [False] * len(grid[0]) for i in range(len(grid)) ]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, visited, i , j)
                    res += 1
                else:
                    continue
        return res
        
    def dfs(self, grid, visited, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
            return
        # four direction
        if not visited[i][j] and grid[i][j] == '1':
            visited[i][j] = True
            self.dfs(grid, visited, i+1, j)
            self.dfs(grid, visited, i-1, j)
            self.dfs(grid, visited, i, j+1)
            self.dfs(grid, visited, i, j-1)
        else:
            return
