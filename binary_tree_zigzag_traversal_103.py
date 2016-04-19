# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = collections.deque()
        stack.append(root)
        cur_level = 0
        while stack:
            size = len(stack)
            cur_level_node = []
            for i in xrange(size):
                cur = stack.popleft()
                cur_level_node.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            if cur_level % 2 == 0:
                cur_level_node.reverse()
            res.append(cur_level_node)
            cur_level += 1
        return res
        
