class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # backtracking
        res = []
        self.dfs(root, res, [])
        return res
        
    def dfs(self, root, res, path):
        if not root:
            if path:
                res.append('->'.join(path))
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            if path:
                res.append('->'.join(path))
            return
        if root.left:
            self.dfs(root.left, res, path)
            path.pop()
        if root.right:
            self.dfs(root.right, res, path)
            path.pop()
