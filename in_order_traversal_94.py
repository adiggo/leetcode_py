class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # in-order sequence
        if root is None:
            return []
        stack = []
        stack.append(root)
        res = []
        node = root

        while node.left is not None:
            stack.append(node.left)
            node = node.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
                node = node.right
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left
        return res
