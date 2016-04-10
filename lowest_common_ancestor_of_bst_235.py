class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: a
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = root.left if root.val > p.val else root.right
        return root
