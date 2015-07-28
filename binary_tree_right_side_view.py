
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        # first traverse all its most right node
        # do level-order bfs
        res = []
        if root is None:
            return res
        stack = []
        stack.append(root)
        while stack:
            helper = []
            last_node = stack[-1]
            res.append(last_node.val)
            while stack:
                node = stack[0]
                stack.remove(node)
                if node.left:
                    helper.append(node.left)
                if node.right:
                    helper.append(node.right)
            stack = helper
        return res
