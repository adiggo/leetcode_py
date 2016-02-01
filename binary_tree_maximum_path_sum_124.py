class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a, b = self.dfs(root)
        return a
    
    def dfs(self, root):
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return root.val, root.val
        left, left_root =  self.dfs(root.left)
        right, right_root =  self.dfs(root.right)
        max_child = max(left, right) if root.left and root.right else left if root.left else right
        max_child_root = max(left_root, right_root) if root.left and root.right else left_root if root.left else right_root
        root_val = root.val if max_child_root < 0 else root.val + max_child_root
        side_val, root_val = root_val, max(root_val, root.val + left_root + right_root)
        return max(max_child, root_val), side_val



    # better approach to store the max_sum into a variable, in the dfs return the side_val
    def __init__(self):
        self.max_sum = -sys.maxint - 1
    def maxPathSum2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max_sum
    
    def dfs2(self, root):
        if not root:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.max_sum = max(self.max_sum, root.val + max(left, 0)+max(right, 0))
        return max(root.val + max(left, 0), root.val + max(right, 0))
