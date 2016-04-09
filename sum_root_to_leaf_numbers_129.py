class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        self.dfs(root, res, root.val)
        return res[0]
        
    def dfs(self, root, curSum, localSum):
        # only increase cursum in the leaf
        if not root.left and not root.right:
            curSum[0] = curSum[0] + localSum
            return
        
        if root.left:
            self.dfs(root.left, curSum, 10*localSum + root.left.val)
        if root.right:
            self.dfs(root.right, curSum, 10*localSum + root.right.val)
    
