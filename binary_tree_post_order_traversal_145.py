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



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# second round --> need to try morris traversal on post order laster..
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # use two stacks
        res = []
        stack1 = []
        stack2 = []
        if not root:
            return res
        stack1.append(root)
        
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            
            if cur.right:
                stack1.append(cur.right)
        
        while stack2:
            res.append(stack2.pop().val)
        return res
