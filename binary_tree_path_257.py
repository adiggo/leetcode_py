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

# another solution, do not create another api
class Solution2:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # backtracking
        if not root:
            return []
        
        if not root.left and not root.right:
            return [str(root.val)]
        res = []
        if root.left:
            left = self.binaryTreePaths(root.left)
            for l in left:
                res.append(str(root.val) + '->' + l)
        if root.right:
            right = self.binaryTreePaths(root.right)
            for r in right:
                res.append(str(root.val) + '->' + r)
        return res
