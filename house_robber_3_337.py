# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # same as house robber 1
        # for each level, there is a max profit we can get
        # left = dfs(root.left) right = dfs(root.right)
        # root.val + left + right, root.left.val + right, root.right.val + left
        if not root:
            return 0
        first, second = self.dfs(root)
        return max(first, second)

    def dfs(self, root):
        if not root:
            return (0, 0)
        if not root.left and not root.right:
            return (root.val, 0)
        # left + right
        left, leftNextLevel = self.dfs(root.left) if root.left else (0, 0)
        right, rightNextLevel = self.dfs(root.right) if root.right else (0, 0)
        return (root.val + leftNextLevel + rightNextLevel, max(left + rightNextLevel, right + leftNextLevel,
                                                               left + right, rightNextLevel + leftNextLevel))
        
