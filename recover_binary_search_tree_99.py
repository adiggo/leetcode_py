class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # do inorder traversal
        nodes = [None, None]
        prev = [None]
        def dfs(root):
            if root:
                dfs(root.left)
                if prev[0] and prev[0].val > root.val:
                    if nodes[0] is None:
                        nodes[0] = prev[0]
                    nodes[1] = root
                prev[0] = root
                dfs(root.right)
        dfs(root)
        nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
