class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.dfs(root, res, 0)
        res.reverse()
        return res
    def dfs(self, root, res, level):
        if not root:
            return
        if level < len(res):
            res[level].append(root.val)
        else:
            # only works for the most left node in each level
            res.append([root.val])
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
