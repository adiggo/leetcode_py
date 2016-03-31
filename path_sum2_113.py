class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, res, [])
        return res
        
    def dfs(self, root, sum, res, cur):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == sum:
                cur.append(root.val)
                res.append(list(cur))
                cur.pop()
            return
        cur.append(root.val)
        isLeft = self.dfs(root.left, sum-root.val, res, cur)
        isRight = self.dfs(root.right, sum-root.val, res, cur)
        cur.pop()
