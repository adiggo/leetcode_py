class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            subroot = stack.pop()
            res.append(subroot.val)
            if subroot.right:
                stack.append(subroot.right)
            if subroot.left:
                stack.append(subroot.left)
        return res
