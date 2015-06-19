class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return None
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        
        return root
