class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        right = self.minDepth(root.right) if root.right else sys.maxint
        left = self.minDepth(root.left) if root.left else sys.maxint
        return min(left, right) + 1
