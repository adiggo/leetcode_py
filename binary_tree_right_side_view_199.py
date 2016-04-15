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
