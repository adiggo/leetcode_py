# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        # the property of a bst is left < central < right
        # so the common ancestry of p and q should be min(p.val, q.val) <= node.val <= max(p.val, q.val)
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)
        # p and q in two side of root
        if not root:
            return None
        if root.val <= larger and root.val >= smaller:
            return root
        # p and q are in one side
        if root.val <= smaller:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val >= larger:
            return self.lowestCommonAncestor(root.left, p, q)
            
