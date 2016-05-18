class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        level = [root]
        while level:
            nextLevel = []
            for i in xrange(len(level)):
                cur = level[i]
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
            if nextLevel:
                res.append(nextLevel[-1].val)
            level = nextLevel
        return res



class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        level = collections.deque()
        level.append(root)
        while level:
            size = len(level)
            for i in xrange(size):
                cur = level.popleft()
                if cur.left:
                    level.append(cur.left)
                if cur.right:
                    level.append(cur.right)
            if level:
                res.append(level[-1].val)
        return res

# second round
class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.helper(1, [0], root, res)
        return res


    def helper(self, depth, maxDepth, root, res):
        if depth > maxDepth[0]:
            maxDepth[0] = depth
            res.append(root.val)
        if root.right:
            self.helper(depth + 1, maxDepth, root.right, res)
        if root.left:
            self.helper(depth +1, maxDepth, root.left, res)
           


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. level order traversal definitely work, but seems a waster of resource 
# 2. optimization: traversal from right child
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.helper(0, root, res)
        return res


    def helper(self, depth, root, res):
        if not root:
            retturn
        if depth == len(res):
            res.append(root.val)
        if root.right:
            self.helper(depth + 1, root.right, res)
        if root.left:
            self.helper(depth +1, root.left, res)
            
