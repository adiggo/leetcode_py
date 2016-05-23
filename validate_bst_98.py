class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -sys.maxint - 1, sys.maxint)

    def isValid(self, root, l, r):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        left = root.left.val if root.left else None
        right = root.right.val if root.right else None
        
        if (not left and right < r and right > root.val) or (not right and left > l and left < root.val):
            return self.isValid(root.left, l, root.val) and self.isValid(root.right, root.val, r)
        
        if (left > l and left < root.val) and (right < r and right > root.val):
            return self.isValid(root.left, l, root.val) and self.isValid(root.right, root.val, r)
        else:
            return False





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # set min and max for each node
        return self.isValidHelper(root, -sys.maxint-1, sys.maxint)
        
    def isValidHelper(self, root, l_min, l_max):
        if not root:
            return True
        left = root.left 
        right = root.right
        if root.val < l_max and root.val > l_min and self.isValidHelper(left, l_min, root.val) and self.isValidHelper(right, root.val, l_max):
            return True
        else:
            return False
