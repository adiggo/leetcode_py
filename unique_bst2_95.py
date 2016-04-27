class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.generate(1, n+1)

    # [left, right)
    def generate(self, l, r):
        res = []
        if l >= r:
            return []
        for i in xrange(l, r):
            left = self.generate(l, i)
            right = self.generate(i + 1, r)
            if left or right:
                if left and right:
                    for left_node in left:
                        for right_node in right:
                            root = TreeNode(i)
                            root.left = left_node
                            root.right = right_node
                            res.append(root)
                else:
                    for j in xrange(max(len(left), len(right))):
                        root = TreeNode(i)
                        root.left = None if not left else left[j]
                        root.right = None if not right else right[j]
                        res.append(root)
        if not res:
            res.append(TreeNode(l))
        return res
