class Solution(object):
    # insert at begining in a list is costing average more time than insert at last
    # to optmize, we can also have another stack, then add all the element in the stack1 into the second stack.
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack1 = []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            res.insert(0, node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return res
