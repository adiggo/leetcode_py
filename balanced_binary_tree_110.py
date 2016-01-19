class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return False
        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True
        
        
    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(right - left) > 1:
            return -1
        return 1 + max(left, right)
